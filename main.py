import os
from pathlib import Path
import time
from dotenv import load_dotenv


from langchain_community.document_loaders import DirectoryLoader, TextLoader

# 2. Partner Packages (Already correct)
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# 3. Core Framework & Chains (Already correct)
from langchain_core.prompts import ChatPromptTemplate
# Load environment variables (like your API keys)
load_dotenv()

from src.generation.llm_chain import create_chain
from src.loader.loaders import extract_markdown_from_image 
from src.ingestion.splitters import CustomSplitter
from src.storage.Vector_store import building_vector_store

cache_dir = Path("C:\\Users\\DELL\\Desktop\\New folder\\src\\data\\processed")
def load_and_process_documents(directory_path: str):
    list_of_unprocessed_text = []
    list_of_text = []
    list_of_metadatas = []
    Chroma_vector_store = None
    cache_file = None
    my_splitter = CustomSplitter(chunk_size=1000, chunk_overlap=200)
    file= Path(directory_path)
    searchable_docs = [".png", ".jpg", ".jpeg"]
    try:
        for index, images in enumerate (file.glob("**/*")):
            if images.suffix.lower() in searchable_docs:
                print(f"Processing image: {images.name}")
                cache_file = cache_dir / f"{images.stem}.md"
                if(cache_file.exists() == False):
                    markdown_content = extract_markdown_from_image(images)
                    with open(cache_file, "w", encoding="utf-8") as f:
                        f.write(markdown_content)
                    chunks = my_splitter.split_text(markdown_content)
                    list_of_unprocessed_text.extend(chunks)
                    for _ in chunks:
                        list_of_metadatas.append({"source": images.name})
                else:
                    with open(cache_file, "r", encoding="utf-8") as f:
                        markdown_content = f.read()
                        chunks = my_splitter.split_text(markdown_content)
                list_of_text.extend(chunks)
    except Exception as e:
        print(f"Error occurred while processing images: {e}")
    Chroma_vector_store = building_vector_store(list_of_unprocessed_text, metadatas=list_of_metadatas, input_collection_name="my_collection", input_persist_directory="C:\\Users\\DELL\\Desktop\\New folder\\src\\data\\vector_db") 
    return Chroma_vector_store, list_of_text
       

                   

if __name__ == "__main__":
    
    directory_path = "C:\\Users\\DELL\\Desktop\\New folder\\src\\data\\raw"
    Chroma_vector_store, list_of_text = load_and_process_documents(directory_path)
    for extracted_text in cache_dir.glob("*.md"):
        with open(extracted_text, "r", encoding="utf-8") as f:
            list_of_text.append(f.read())
    chain = create_chain(Chroma_vector_store = Chroma_vector_store, list_of_text = list_of_text)
    query = input("Enter your query: ")
    result = chain.invoke(query)
    print(result)
