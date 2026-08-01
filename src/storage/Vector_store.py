import time
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def building_vector_store(chunks, metadatas, input_collection_name="my_collection", input_persist_directory="chroma_db"):
    embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    
    print("\nConnecting to Vector Database...")
    # 1. Initialize the empty database connection first
    vector_store = Chroma(
        collection_name=input_collection_name,
        persist_directory=input_persist_directory,
        embedding_function=embedding_model
    )
    
    # 2. If there are no new chunks, just return the database immediately
    if not chunks:
        print("No new chunks to embed. Database is up to date!")
        return vector_store

    # 3. The Batching Engine (Max 90 chunks at a time)
    batch_size = 90 
    
    for i in range(0, len(chunks), batch_size):
        # Slice the master lists into smaller batches
        batch_texts = chunks[i : i + batch_size]
        batch_metadatas = metadatas[i : i + batch_size]
        
        print(f"🧠 Embedding chunks {i + 1} to {i + len(batch_texts)} out of {len(chunks)}...")
        
        # Send only the small batch to Google
        vector_store.add_texts(texts=batch_texts, metadatas=batch_metadatas)
        
        # If there are still more chunks left to process, pause for 60 seconds
        if i + batch_size < len(chunks):
            print("⏳ Google API limit reached. Waiting 60 seconds for quota to reset...")
            time.sleep(60)
            
    print("✅ All chunks successfully embedded!")
    return vector_store