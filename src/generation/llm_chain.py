from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def create_chain(retriever):
    llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.7,
    )
    template_setting = "You are a helpful assistant. Answer the user's question using ONLY the provided context. If the answer is not in the context, explicitly say 'I don't know'."
    template = ChatPromptTemplate.from_messages([
        ("system", template_setting),
        ("human", "Context: {context}\nQuestion: {question}\n")
    ])
    chain = {"context": retriever, "question": RunnablePassthrough()}| template | llm | StrOutputParser()
    return chain
