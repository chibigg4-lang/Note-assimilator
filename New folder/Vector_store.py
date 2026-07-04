from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from ingestion.splitters import chunks
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector_store = Chroma("my_collection", embedding_model)
for chunk in chunks:
    vector_store.add_documents([doc])
