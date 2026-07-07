from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def building_vector_store(chunks, input_collection_name="my_collection", input_persist_directory="chroma_db"):
    embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embedding_model,
        collection_name=input_collection_name,
        persist_directory=input_persist_directory
    )
    return vector_store
