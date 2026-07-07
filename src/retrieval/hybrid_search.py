from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
def Hybrid_search(vector_store, chunks):
    vector_search = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )
    bm25_search = BM25Retriever.from_texts(texts=chunks)
    bm25_search.k = 4
    return EnsembleRetriever(retrievers=[vector_search, bm25_search], weights=[0.6, 0.4])

