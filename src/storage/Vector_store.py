from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def building_vector_store(chunks):
    embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vector_store = Chroma.from_documents(
        documents=chunks, 
        embedding=embedding_model, 
        collection_name="my_collection"
    )
    return vector_store
