import os
from pathlib import Path
from dotenv import load_dotenv


from langchain_community.document_loaders import DirectoryLoader, TextLoader

# 2. Partner Packages (Already correct)
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# 3. Core Framework & Chains (Already correct)
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (like your API keys)
load_dotenv()

from src.loader.loaders import extract_markdown_from_image 
from src.ingestion.splitters import CustomSplitter
from src.storage.Vector_store import building_vector_store
from src.retrieval.hybrid_search import Hybrid_search
from src.generation.llm_chain import create_chain

def load_and_process_documents(directory_path: str):
   list_of_chunks = []
   Chroma_vector_store = None
   my_splitter = CustomSplitter(chunk_size=1000, chunk_overlap=200)
   file= Path(directory_path)
   searchable_docs = [".png", ".jpg", ".jpeg", ".pdf", ".txt"]
   try:
        for images in file.glob("**/*"):
            if images.suffix.lower() in searchable_docs:
                markdown_content = extract_markdown_from_image(images)
                chunks = my_splitter.split_text(markdown_content)
                list_of_chunks.extend(chunks)
                Chroma_vector_store = building_vector_store(chunks, input_collection_name="my_collection", input_persist_directory="C:\\Users\\DELL\\Desktop\\New folder\\src\\data\\vector_db")
   except Exception as e:
        print(f"Error occurred while processing images: {e}")
   return list_of_chunks, Chroma_vector_store
       

                   

if __name__ == "__main__":
    directory_path = "C:\\Users\\DELL\\Desktop\\New folder\\src\\data\\raw"
    list_of_chunks, Chroma_vector_store = load_and_process_documents(directory_path)
    Emsemble_retriever = Hybrid_search(Chroma_vector_store, list_of_chunks)
    chain = create_chain(Emsemble_retriever)
    query = input("Enter your query: ")
    result = chain.invoke(query)
    print(result)