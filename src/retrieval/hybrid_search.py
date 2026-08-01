from langchain_classic.retrievers import EnsembleRetriever

def Hybrid_search(vector_store, prebuilt_bm25):
    vector_search = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 10}
    )
    return EnsembleRetriever(
        retrievers=[vector_search, prebuilt_bm25], 
        weights=[0.4, 0.6]
    )