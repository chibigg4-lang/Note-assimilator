from functools import partial
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_classic.retrievers import BM25Retriever
from langsmith import traceable
from src.retrieval.query_routing import classifying
from src.retrieval.hybrid_search import Hybrid_search
# from src.retrieval.compressor import Cross_encoder_reranker

classifier = classifying()
@traceable
def dynamic_routing_retriever(question: str, Chroma_vector_store, prebuilt_bm25):
    routing_data = classifier.invoke(question)
    routed_data = routing_data.model_dump()

    Emsemble_retriever = Hybrid_search(Chroma_vector_store, prebuilt_bm25)
    
    list_of_keywords = routed_data["keywords"]
    search_lists = list_of_keywords + [question]
    
    for keyword in search_lists:
        print(keyword + "\n")
        
    relevant_docs = Emsemble_retriever.batch(search_lists)
    unique_docs = []
    seen_content = set()
    
    for doc_list in relevant_docs:
        for doc in doc_list:
            if doc.page_content not in seen_content:
                seen_content.add(doc.page_content) 
                unique_docs.append(doc)
    
    if routing_data.category == "linear algebra":
        pass
    elif routing_data.category == "Calculus":
        pass
    elif routing_data.category == "Statistics":
        pass
        
    for doc in unique_docs:
        print(doc.page_content + "\n")
        
    return unique_docs


def create_chain(Chroma_vector_store, list_of_text):
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0.7,
    )
    
    template_setting = "You are a helpful assistant. Answer the user's question using ONLY the provided context. If the answer is not in the context, explicitly say 'I don't know'."
    template = ChatPromptTemplate.from_messages([
        ("system", template_setting),
        ("human", "Context: {context}\nQuestion: {question}\n")
    ])
    
    bm25_retriever = BM25Retriever.from_texts(texts=list_of_text)
    bm25_retriever.k = 10
    

    bound_retriever = partial(
        dynamic_routing_retriever, 
        Chroma_vector_store=Chroma_vector_store, 
        prebuilt_bm25=bm25_retriever
    )
    
    routed_retriever = RunnableLambda(bound_retriever)
    
    chain = (
        {"context": routed_retriever, "question": RunnablePassthrough()} 
        | template 
        | llm 
        | StrOutputParser()
    )
    
    return chain