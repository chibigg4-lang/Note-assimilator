# LangChain Chroma Core Functions Reference

---

# I. Core Components

## Document(page_content, metadata)

### Purpose
The foundational LangChain object used to hold text and its associated tags before putting it into a vector store.

### Inputs

- *page_content (String)* — The actual raw text content.
- *metadata (Dictionary, Optional)* — Tags for filtering (e.g., {"source": "wiki", "page": 5}).

### Output

- A LangChain Document object.

### When to use

- Whenever you need to manually package text to feed into a LangChain pipeline or vector store.

---

# II. Vector Store Initialization
## Chroma(collection_name, embedding_function, persist_directory)

### Purpose

The core constructor that initializes a connection to a vector database instance. Unlike Chroma.from_documents() (which actively ingests and embeds new data), this function is primarily used to establish a link between your Python script and an existing storage location.

---

### Inputs

#### collection_name (String)

The specific "table" or bucket of vectors you want to access. You can store multiple collections (e.g., "calculus_notes" and "cpp_notes") inside the same database folder.

---

#### embedding_function (Object)

Your initialized embedding model (e.g., GoogleGenerativeAIEmbeddings). Critical constraint: This must be the exact same embedding model you used to build the database. If you built it with Gemini and try to read it with OpenAI, the math will catastrophically fail.

---

#### persist_directory (String, Optional)

The local folder path where the database SQLite files are saved (e.g., "./chroma_db").

---

### The Connection Logic (Connect vs. Create)

When you run this function, LangChain executes a strict decision tree to determine whether it should connect to old data or build something new:

#### The "Full Connect" (Mount existing data)

If the persist_directory exists on your hard drive, AND the collection_name exists inside it, Chroma simply mounts the database. No data is overwritten, and it is instantly ready to be queried.

#### The "New Table" (Connect to DB, Create Collection)

If the persist_directory exists, but the collection_name does not exist inside it, Chroma mounts the database folder but creates a brand new, empty collection alongside your other ones.

#### The "Hard Boot" (Create from scratch)

If the persist_directory folder does not exist on your computer at all, Chroma creates the folder, generates the base SQLite database files, and initializes a brand new, empty collection.

#### The "Ephemeral Boot" (In-Memory)

If you leave persist_directory completely blank, Chroma creates a temporary database in your computer's RAM. It will work perfectly while your code runs, but the second the Python script stops, the database is permanently deleted.

---

### Output

A LangChain Chroma VectorStore object.

---

### When to use

In your production main.py file. Once your ingestion pipeline has successfully embedded your notes and saved them to your hard drive, you stop using .from_documents(). Instead, you use this standard constructor to instantly boot up your app and query your data without paying API costs to re-embed the Markdown files every time you restart the script.

---

## Chroma.from_documents(documents, embedding, persist_directory, collection_name)

### Purpose

A shortcut function that creates a new database, calculates the embeddings for a list of Documents, and saves them all in one step.

### Inputs

- *documents (List of Document objects)* — The text you want to add.
- *embedding (Object)* — Your initialized embedding model.
- *persist_directory (String, Optional)* — Where to save the database locally.
- *collection_name (String, Optional)* — The name of the collection.

### Output

- A fully populated LangChain Chroma VectorStore object.

### When to use

- When you are building a new database from scratch and have your data ready as LangChain Documents.

---

## Chroma.from_texts(texts, embedding, metadatas, persist_directory)

### Purpose

Similar to from_documents, but allows you to pass raw strings instead of wrapping them in Document objects first.

### Inputs

- *texts (List of Strings)* — The raw text chunks.
- *embedding (Object)* — Your initialized embedding model.
- *metadatas (List of Dictionaries, Optional)* — The metadata corresponding to each text chunk.

### Output

- A populated LangChain Chroma VectorStore object.

### When to use

- When you have lists of raw strings (e.g., from an API scraper) and want to skip the step of manually creating Document objects.

---

# III. Data Operations

## vector_store.add_documents(documents, ids=None)

### Purpose

Ingests new LangChain Documents into an already existing vector store.

### Inputs

- *documents (List of Document objects)* — The new documents to add.
- *ids (List of Strings, Optional)* — Unique string identifiers for each document. If omitted, LangChain automatically generates random UUIDs for you.

### Output

- A list of the string IDs assigned to the added documents.

### When to use

- When updating an existing database with new information.

---

## vector_store.delete(ids)

### Purpose

Removes specific documents from the vector store.

### Inputs

- *ids (List of Strings)* — The unique IDs of the documents to remove.

### Output

- None.

### When to use

- When purging outdated information.

Note: You must have manually provided and saved the IDs when you added the documents in order to delete them this way.


---
## chroma_db.get()

### Purpose

Retrieves raw records directly from the Chroma database collection without performing a similarity or vector search. It acts as a direct query to view the underlying data storage.

---

### Inputs

#### ids (List of Strings, Optional)

Specific unique chunk IDs you want to fetch.

---

#### where (Dictionary, Optional)

A metadata filter to return only specific records (e.g., {"source": "MA1522_Notes_9.jpg"}).

---

#### limit (Integer, Optional)

The maximum number of records to pull at once.

---

#### include (List of Strings, Optional)

Specifies exactly which columns to return.

Defaults to:

["metadatas", "documents"]

(To retrieve the raw 768-dimensional vectors, you must explicitly include "embeddings").

---

### Output

A Dictionary of Lists (columnar format) where index positions correspond to the same chunk across all lists.

Example:

{
    "ids": [...],
    "documents": [...],
    "metadatas": [...],
    "embeddings": [...]
}

---

### When to use

- Whenever you need to audit the total contents of your database to see exactly what files have been processed.

- When verifying that your custom text splitters and metadata tagging worked correctly during ingestion.

- When you need to retrieve specific chunk IDs so you can target them for deletion or updates.
---

# IV. Search & Retrieval

## vector_store.similarity_search(query, k=4, filter=None)

### Purpose

Translates a user's string question into a vector, searches the database, and returns the most relevant documents.

### Inputs

- *query (String)* — The user's human-readable question.
- *k (Integer, Optional)* — How many top matching documents to return (defaults to 4).
- *filter (Dictionary, Optional)* — Metadata tags to narrow down the search (e.g., {"source": "book"}).

### Output

- A flat list of LangChain Document objects.

### When to use

- When you want to manually retrieve text to print to the console or inspect.

---

## vector_store.similarity_search_with_score(query, k=4, filter=None)

### Purpose

Identical to similarity_search, but also returns the mathematical distance score so you can see how closely it matched.

### Inputs

- Same as similarity_search.

### Output

- A list of tuples:
  - (Document, Float Score)

### When to use

- When debugging retrieval quality.
- When setting thresholds.

Example:

Only use answers with a distance score below 0.5.



---

# LANGCHAIN RAG PIPELINE CORE FUNCTIONS REFERENCE

---

# I. DOCUMENT PRE-PROCESSING (CHUNKING)

LangChain provides a whole family of Text Splitters.

While they all have different strategies for how they cut the text, they all share the exact same output format and are executed using the exact same split_documents() function.

---

## 1. RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)

### Purpose

- The industry standard.
- Tries to break text using paragraphs first, then sentences, then words.
- Keeps related concepts together as much as possible.

### Inputs

- *chunk_size (Integer)* → Maximum characters per chunk.
- *chunk_overlap (Integer)* → Number of overlapping characters.

### When to use

- Default choice for general text, articles, PDFs.

---

## 2. TokenTextSplitter(chunk_size, chunk_overlap)

### Purpose

- Cuts text based on LLM token count rather than character count.

### Inputs

- *chunk_size (Integer)* → Maximum tokens.
- *chunk_overlap (Integer)*

### When to use

- When working with strict context window limits.
- When chunks must align with OpenAI/Gemini token restrictions.

---

## 3. MarkdownHeaderTextSplitter(headers_to_split_on)

### Purpose

- Splits documents according to markdown structure.
- Uses headers such as # Header 1 or ## Header 2 instead of character counts.

### Inputs

- *headers_to_split_on (List of Tuples)*

Example:

[("#", "Header 1")]

### When to use

- Structured Markdown documents.
- GitHub README files.
- Notion exports.

---

## Universal Execution Function

### splitter.split_documents(documents)

#### Purpose

- Executes the splitting strategy on raw documents.
- All LangChain text splitters use this command.

#### Inputs

- *documents (List of Document objects)*

#### Output

- A larger list of smaller LangChain Document objects ready for embedding.

#### When to use

- After loading files.
- After initializing a splitter.
- Before sending data to ChromaDB.

---

# II. KNOWLEDGE BASE INTEGRATION (RETRIEVAL)

## vector_store.as_retriever()

vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={}
)

### Purpose

- Converts a vector database into a standardized Retriever.
- Allows the pipeline to automatically query the database and fetch documents.

---

## search_type

### 1. "similarity" (Default)

#### Purpose

- Standard vector similarity search.
- Returns the most mathematically similar documents.

---

### 2. "mmr" (Maximal Marginal Relevance)

#### Purpose

- Optimizes for diversity.
- Penalizes documents that are too similar to each other.
- Prevents retrieving multiple chunks saying the same thing.

---

### 3. "similarity_score_threshold"

#### Purpose

- Returns only documents above a minimum similarity score.
- Does not guarantee a fixed number of documents.

---

## search_kwargs

### k (Integer)

#### Purpose

- Final number of documents returned.

Example:

{"k": 4}

Works with:

- similarity
- mmr
- similarity_score_threshold

---

### filter (Dictionary)

#### Purpose

- Filters documents by metadata before similarity calculation.

Example:

{"filter": {"source": "wiki"}}

Works with:

- similarity
- mmr
- similarity_score_threshold

---

### fetch_k (Integer)

#### Purpose

- Used only by MMR.
- Number of candidate documents initially retrieved before diversity filtering.

#### Default

- 20

---

### lambda_mult (Float)

#### Purpose

- Used only by MMR.
- Controls relevance vs diversity balance.

#### Values

- 0.0 = maximum diversity
- 1.0 = behaves like standard similarity

#### Default

- 0.5

---

### score_threshold (Float)

#### Purpose

- Used only by similarity_score_threshold.
- Minimum similarity score required.

Example:

{"score_threshold": 0.8}

---

## Output

- LangChain VectorStoreRetriever object.

## When to use

- Right after loading or creating a vector database.
- Controls how strict, broad, or diverse retrieval should be.
- --
# Two stages retriever 
## ContextualCompressionRetriever(base_compressor, base_retriever)

### Purpose

Orchestrates a two-stage retrieval pipeline by first querying a fast, wide-net search engine and then passing those raw results through a scoring, filtering, or compression mechanism before handing the final text to the system.

### Inputs

#### base_compressor (BaseDocumentCompressor)

The module responsible for scoring, filtering, splitting, or rewriting the documents after the initial fetch.

#### base_retriever (BaseRetriever)

The initial search engine tasked with pulling a large batch of candidate documents quickly (e.g., your hybrid vector-keyword search).

### Output

A unified ContextualCompressionRetriever object that automates the entire two-stage lifecycle when its .invoke(query) or .ainvoke(query) method is called.

### When to use

When you want to implement a multi-stage search workflow (like fetching 20 documents via hybrid search and refining them down to the best 3) to maximize retrieval precision while keeping the final LLM prompt context clean and free of irrelevant noise.

### Import

from langchain.retrievers import ContextualCompressionRetriever


### Stage 1: Base Retriever Options (Expanded)

| Retriever Option                                                 | Inputs                                                                                                                                                                                                               | Output                                                                              | When to Use                                                                                                                                                                                                        |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Vector Store Retriever**<br>`vector_store.as_retriever(...)`   | search_type *(String)*: Method to match vectors (e.g., "similarity").<br><br>`search_kwargs` (Dict): Parameters like {"k": 20}.                                                                                | A VectorStoreRetriever object wrapped around your database.                       | Use when retrieving documents based on deep semantic or conceptual meaning rather than exact word matching.                                                                                                        |
| **Keyword Retriever**<br>`BM25Retriever.from_texts(...)`         | texts (List[str]): The corpus of document chunks to index.<br><br>`k` *(Int, Optional)*: Number of documents to retrieve.                                                                                        | A BM25Retriever object configured for statistical sparse keyword search.          | Use when matching exact technical words, code syntax, jargon, or variables that semantic models might blur over.                                                                                                   |
| **Hybrid Retriever**<br>`EnsembleRetriever(...)`                 | retrievers (List[BaseRetriever]): A list of distinct retrievers to combine.<br><br>`weights` (List[float]): Priority weights for tie-breaking.                                                                 | An EnsembleRetriever object that merges the output of multiple search strategies. | Use when you want to combine semantic vector understanding with the strict literal accuracy of keyword matching.                                                                                                   |
| **Multi-Query Retriever**<br>`MultiQueryRetriever.from_llm(...)` | retriever (BaseRetriever): Your base search engine.<br><br>`llm` (BaseLanguageModel): The LLM used to rewrite queries.                                                                                         | A MultiQueryRetriever object that automates query expansion.                      | Use when user queries might be vague or poorly phrased; it uses an LLM to generate multiple perspectives on the query and takes the unique union across all queries to get a richer set of results.                |
| **Parent Document Retriever**<br>`ParentDocumentRetriever(...)`  | vectorstore (VectorStore): Database for small chunks.<br><br>`docstore` (BaseStore): Storage for the large parent documents.<br><br>`child_splitter` (TextSplitter): Splitter for precise search chunks.     | A ParentDocumentRetriever object.                                                 | Use when you want to retrieve small chunks based on a query and subsequently look up their parent document IDs to return the larger original documents or predefined larger chunks, ensuring contextual integrity. |
| **Self-Query Retriever**<br>`SelfQueryRetriever.from_llm(...)`   | llm (BaseLanguageModel): The LLM used to extract filters.<br><br>`vectorstore` (VectorStore): Your underlying database.<br><br>`metadata_field_info` (List[AttributeInfo]): Schema describing your metadata. | A SelfQueryRetriever object capable of natural-language metadata filtering.       | Use when you need to transform natural language queries into structured queries that include semantic search criteria and metadata filters based on fields like date, source, or tags.                             |

### Stage 2: Base Compressor Options 

| Compressor Option                                            | Inputs                                                                                                                                                                                                                             | Output                                 | When to Use                                                                                                                                                                                                  |
| :----------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Deep Re-ranker**<br>`CrossEncoderReranker(...)`            | model (BaseCrossEncoder): The local model object (like bge-reranker-base).<br><br>`top_n` *(Integer)*: Number of high-scoring documents to keep.                                                                             | A CrossEncoderReranker object.       | Use when you need absolute maximum accuracy in ordering results based on deep logical relationships, and you have the local hardware to run it.                                                              |
| **Sequential Pipeline**<br>`DocumentCompressorPipeline(...)` | transformers (List): A sequence of individual components (e.g., splitter -> filter -> reranker) executed in order.                                                                                                             | A DocumentCompressorPipeline object. | Use when a single compressor isn't enough, and you need to apply multiple data cleaning steps before handing context to the LLM.                                                                             |
| **LLM Content Filter**<br>`LLMChainExtractor.from_llm(...)`  | llm (BaseLanguageModel): The LLM engine tasked with reading and parsing the raw text blocks.                                                                                                                                   | An LLMChainExtractor object.         | Use when retrieved chunks contain conversational filler, and you want to shrink the text footprint down to just pure facts before the final prompt.                                                          |
| **Embeddings Filter**<br>`EmbeddingsFilter(...)`             | embeddings (Embeddings): The embedding model used to score text.<br><br>`similarity_threshold` *(Float)*: The minimum similarity score required to keep a document.<br><br>`k` (Integer, Optional): Max documents to return. | An EmbeddingsFilter object.          | Use for a fast and computationally cheap filter that simply drops retrieved documents if their embedding similarity score falls below a specific threshold (e.g., 0.75).                                     |
| **Cohere Rerank**<br>`CohereRerank(...)`                     | cohere_api_key *(String)*: Your Cohere API key.<br><br>`model` (String): The reranker model name.<br><br>`top_n` (Integer, Optional): The number of results to return.                                                       | A CohereRerank object.               | Use when you want a highly effective, hosted API cross-encoder architecture that is widely used for production RAG pipelines.                                                                                |
| **FlashRank Rerank**<br>`FlashrankRerank(...)`               | model *(String, Optional)*: The local model name to run (e.g., ms-marco-MiniLM-L-12-v2).<br><br>`top_n` (Integer, Optional): The number of results to return.                                                                | A FlashrankRerank object.            | Use for a small, ultra-lightweight cross-encoder that runs completely locally. It requires zero API calls, making it perfect for applications with strict data privacy requirements.                         |
| **LLMLingua Compressor**<br>`LLMLinguaCompressor(...)`       | model_name *(String)*: The HuggingFace model to use.<br><br>`target_token` (Integer): The target number of compressed tokens.<br><br>`instruction` (String, Optional): The prompt instruction for the LLM.                   | An LLMLinguaCompressor object.       | Use to shrink the physical text down to its most critical tokens. This saves money on language model API calls by drastically reducing the amount of text you have to feed into the final generation prompt. |
# Universal Retriever Execution Functions

## 1. retriever.invoke(input_query)

### Purpose

- The standard, modern execution function for any LangChain retriever object.
- Fully integrated with the LangChain Expression Language (LCEL) standard.

### Inputs

- *input_query (String)*

### Output

- A sorted list of LangChain Document objects matched from the database.

### When to use

- To run an individual test query through your retriever manually.
- This is the function called implicitly behind the scenes when a retriever runs inside an active RAG chain.

---

## 2. retriever.batch([query_1, query_2])

### Purpose

- Runs multiple search queries completely in parallel.

### Inputs

- List of Strings.

### Output

- A nested list of Document lists.

### When to use

- Batched workloads.
- Testing multiple search iterations concurrently.

---

## 3. retriever.ainvoke(input_query)

### Purpose

- The asynchronous variant of invoke().

### Inputs

- *input_query (String)*

### Output

- A Python coroutine object resolving to a list of Document objects.

### When to use

- Async production environments.
- FastAPI.
- Streamlit concurrent UIs.

---

## 4. retriever.abatch([query_1, query_2])

### Purpose

The asynchronous version of .batch().

Combines parallel query grouping with non-blocking async operations.

### Inputs

- A list of strings.

### Output

- An awaitable Python coroutine resolving to a nested list of Document lists.

### When to use

- Large-scale concurrent workloads.

---

## 5. retriever.stream(input_query)

### Purpose

Yields retrieved chunks sequentially as they become available.

### Inputs

- *input_query (String)*

### Output

- An iterator yielding lists of Document objects chunk-by-chunk.

### When to use

- UI updates.
- Intermediate processing before all retrieval completes.

---

## BM25Retriever.from_documents(documents)

### Purpose

- Instantiates an in-memory, keyword-based (lexical) search engine directly inside your computer's RAM.
- Performs exact word-for-word string matching based on term frequency and document length statistics instead of semantic meaning.

### Parameters

#### documents (List[Document])

Purpose:

The list of raw LangChain Document text chunks that the algorithm counts and indexes into memory on initialization.

### Key Properties

#### k (Integer)

Purpose:

Controls how many total exact-match documents are pulled from the tokenized index when executing a search.

Example:

retriever.k = 4

---

### Output

LangChain BM25Retriever object.
## EnsembleRetriever(retrievers, weights)  
  
### Purpose  
  
- Acts as a master orchestration wrapper that forces multiple distinct search strategies (e.g., dense vector search and sparse keyword search) to execute concurrently.  
  
- Seamlessly merges the disparate result lists from these underlying engines into a single, unified document stream.  
  
- Normalizes fundamentally incompatible scoring systems (such as Cosine Similarity decimal scores and BM25 statistical whole-number scores) by employing the *Reciprocal Rank Fusion (RRF)* algorithm.  
  
- Rather than relying on raw retrieval scores, RRF recalculates ranking importance based on each document's finishing position (rank) across all participating retrievers.  
  
---  
  
### Inputs  
  
#### retrievers (List[BaseRetriever])  
  
##### Purpose  
  
- Accepts a list of instantiated LangChain retriever objects that will be executed in parallel.  
  
- While most commonly used with two retrieval systems (one dense semantic retriever and one sparse keyword retriever), it can theoretically combine any number of retrievers.  
  
##### Example  
  
retrievers = [  
keyword_retriever,  
vector_retriever  
]  
  
---  
  
#### weights (List[Float])  
  
##### Purpose  
  
- Assigns a fractional prioritization multiplier to the final RRF score contributed by each retriever.  
  
- Allows fine-grained control over how much influence each retrieval strategy has on the final ranking.  
  
- Useful when your application should favor:  
- Exact keyword matches (higher BM25 weight)  
- Semantic meaning (higher vector retriever weight)  
- A balanced hybrid approach  
  
##### Constraints  
  
- The length of the weights list must exactly match the length of the retrievers list.  
  
- All weight values combined must sum to exactly *1.0*.  
  
##### Example  
  
weights = [0.7, 0.3]  
  
Meaning:  
  
- 70% of ranking influence comes from the first retriever.  
- 30% of ranking influence comes from the second retriever.  
  
---  
  
### Output  
  
- *LangChain EnsembleRetriever object*
---
### 1. reranker.compress_documents(documents, query)

*Purpose*

- The standard execution function for evaluating, scoring, and sorting a batch of text chunks against the user's specific query.
    
- Instead of just pulling data, it compares the query string directly against every single document in the documents list simultaneously to calculate a high-precision relevance score.
    

*Inputs*

- documents (List[Document]) — The raw pool of LangChain Document objects (usually from your Hybrid Search deduplication set).
    
- query (String) — The original user question to score the documents against.
    

*Output*

- A sorted, reduced list of LangChain Document objects (highest relevance score at index 0).
    

*When to use*

- To manually pass your unified pool of hybrid-search documents through the cross-encoder.
    
- This is the function called implicitly behind the scenes when a reranker runs inside a ContextualCompressionRetriever.
    

### 2. reranker.acompress_documents(documents, query)

*Purpose*

- The asynchronous variant of compress_documents().
    
- Executes the heavy transformer scoring process without blocking the main event loop.
    

*Inputs*

- documents (List[Document])
    
- query (String)
    

*Output*

- A Python awaitable coroutine object resolving to a sorted list of Document objects.
    

*When to use*

- Async production environments (e.g., FastAPI, async LangServe architectures).
    
- When multiple users are querying the RAG pipeline simultaneously and you cannot afford to freeze the server during the reranking step.
    

### 3. CrossEncoderReranker(model=..., top_n=...)

*Purpose*

- Instantiates the reranking engine by pairing a raw scoring model with a pruning threshold.
    

*Parameters*

- model (BaseCrossEncoder)
    
    - *Purpose:* The initialized scoring engine (e.g., HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-base")). This is the brain that does the actual math.
        
- top_n (Integer)
    
    - *Purpose:* The hard limit on how many documents survive the reranking process to be passed to the LLM.
        

### Key Properties

*top_n (Integer)*

- *Purpose:*
    
    - Controls the maximum number of documents that make it out of the compressor. If you feed compress_documents a list of 50 unique chunks, and top_n = 4, the reranker will score all 50, discard the bottom 46, and return only the top 4.
        
- *Example:*
    
    Python
    
    
    reranker.top_n = 4
    
    

*model (Object)*

- *Purpose:*
    
    - Holds the underlying HuggingFace neural network wrapper. You rarely interact with this property directly after initialization, but it dictates the speed and accuracy of the compress_documents function based on the specific transformer model you loaded.
# III. LANGUAGE MODEL (LLM) INITIALIZATION

## 1. init_chat_model(model, temperature)

### Purpose

- Modern universal constructor for chat models.
- Automatically chooses the provider based on model name.
- Works across OpenAI, Google, Anthropic, etc.

### Inputs

#### model (String)

Example:

"gpt-4o-mini"

#### temperature (Float)

Range:

text
0.0 → 1.0

Meaning:

- 0.0 = highly factual
- 1.0 = highly creative

### Output

- LangChain Runnable LLM object.

### When to use

- Recommended modern approach.
- Easy provider switching.

---

## 2. ChatGoogleGenerativeAI(model, temperature)

(or ChatOpenAI)

### Purpose

- Provider-specific LLM initialization.
- Older approach.

### Inputs

- model (String)
- temperature (Float)

### Output

- LangChain Runnable LLM object.

### When to use

- When explicitly using provider-specific classes.

---

# IV. PROMPT ENGINEERING

LangChain provides specialized template structures designed to communicate effectively with different generations of language models.

Modern LLMs are trained on conversation histories rather than flat text blocks.

---

## 1. ChatPromptTemplate.from_messages(message_list)

### Purpose

- Industry standard for modern RAG pipelines.
- Structures prompts into explicit conversational segments.
- Formats prompts natively into provider APIs.

### Inputs

#### message_list (List of Tuples)

Example:

[
    ("system", "You are a strict corporate HR assistant. Use this context: {context}"),
    ("human", "Question: {question}")
]

### Detailed Conversational Role Breakdown

#### system

Meaning:

Defines the core persona, tone, operational boundaries, restrictions, and foundational rules.

Usage in RAG:

Pass retrieved chunks via {context} and guardrails.

#### human / user

Meaning:

Represents end-user input.

Usage in RAG:

Pass {question}.

#### ai / assistant

Meaning:

Historical model responses.

Usage in RAG:

Few-shot examples.

### Output

- LangChain ChatPromptTemplate object.

### When to use

- Default choice for modern chat-tuned models.
- Reduces prompt injection risk.

---

## 2. PromptTemplate.from_template(template_string)

### Purpose

- Creates a flat, single-string template.
- Automates variable extraction.

### Inputs

#### template_string (String)

Example:

"Answer the following question: {question} using only this data: {context}"

### Output

- LangChain PromptTemplate object.

### When to use

- Older completion models.
- Utility strings.

### Crucial Technical Constraints

#### Brace Escaping Rule

Variable placeholder:

{my_variable}

Literal braces:

{{ "json_key": "json_value" }}

---

## 3. MessagesPlaceholder(variable_name)

### Purpose

Acts as a structural placeholder inside a ChatPromptTemplate.

### Inputs

#### variable_name (String)

Example:

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

### Output

- LangChain MessagesPlaceholder object.

### When to use

- Production chatbots.
- Conversational memory.

---

# Universal Prompt Formatting & Execution Methods

## 1. prompt.invoke(input_dict)

### Purpose

- Standard LCEL execution approach.
- Compiles variables.

### Inputs

{
  "context": "Text data...",
  "question": "User query..."
}

### Output

- PromptValue object.

---

## 2. prompt.format_messages(kwargs)

### Purpose

Resolves placeholders while maintaining roles.

### Output

- List of LangChain Message instances.

---

## 3. prompt.format(kwargs)

### Purpose

Flattens the template into a single text string.

### Output

- String

---

## 4. prompt.partial(kwargs)

### Purpose

Pre-fills a subset of variables.

### Output

- New PromptTemplate or ChatPromptTemplate.

### When to use

- Binding environment variables.
- Current dates.
- Static context.

---

# V. OUTPUT PARSING

## StrOutputParser()

### Purpose

- Extracts only the text from the LLM response.
- Removes wrapper objects.

### Inputs

- None

### Output

- OutputParser object.

### When to use

- Always place at the end of a RAG chain.
- Produces a clean printable string.

---


# VI. DATA ROUTING (LCEL)

## RunnablePassthrough()

### Purpose

- Transparent pipe inside a chain.
- Passes user input unchanged.

### Inputs

- None

### Output

- Runnable object.

### When to use

- Building dictionaries for prompt templates.
- Passing user question directly to the LLM while the retriever supplies context.

---

# COMMON RAG FLOW

text
Documents
↓
Text Splitter
↓
split_documents()
↓
Embeddings
↓
Chroma Vector Store
↓
as_retriever()
↓
Retriever ──→ [invoke() / ainvoke() / batch()]
↓
Prompt Template
↓
LLM
↓
StrOutputParser()
↓
Final Answer

# Tokenization & Token Budget Management

---

## tiktoken.encoding_for_model(model_name)

### Purpose

- Fetches the exact tokenizer dictionary used by a specific language model.

- Translates raw text into the same numerical token representation that the target LLM uses internally.

- Ensures that all token-count calculations match the provider's billing and context-window calculations exactly.

---

### Inputs

#### model_name (String)

##### Purpose

- Specifies the exact identifier of the target language model.

##### Example

"gpt-4o-mini"

---

### Output

- A *tiktoken Encoding object* containing the tokenizer rules used by the specified model.

---

### When to Use

- When initializing a token-counting pipeline.

- Before implementing chunking logic based on token limits.

- When estimating prompt size, retrieval size, or API costs.

- Whenever accurate token calculations are required.

---

### Example

import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o-mini")

---

### Why It Matters

Different language models can tokenize the exact same text differently.

For example:

text
"Artificial Intelligence"

might become:

text
Model A → 2 tokens
Model B → 4 tokens

Using the correct tokenizer ensures your calculations match the model's actual context window and pricing behavior.

---

## encoding.encode(text)

### Purpose

- Converts a raw text string into its corresponding token IDs.

- Applies the tokenization rules stored inside the active Encoding object.

- Allows precise measurement of token length before sending data to an LLM.

---

### Inputs

#### text (String)

##### Purpose

- The raw text content that needs to be tokenized.

##### Examples

- Document chunks
- Prompt templates
- User queries
- Retrieved context

---

### Output

- A list of integer token IDs.

Example:

[9906, 1917, 0]

---

### When to Use

- Before sending text to an LLM.

- Before storing chunks in a vector database.

- During chunk-size validation.

- During prompt budget calculations.

---

### Example

tokens = encoding.encode("Hello world!")
token_count = len(tokens)

---

### Typical Workflow

text
    ↓
encoding.encode(text)
    ↓
[token_id_1, token_id_2, ...]
    ↓
len(tokens)
    ↓
Total Token Count

---

## RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size, chunk_overlap)

### Purpose

- Creates a RecursiveCharacterTextSplitter that measures chunk size using tokens rather than characters.

- Preserves the intelligent splitting behavior of RecursiveCharacterTextSplitter while enforcing token-based limits.

- Helps guarantee that document chunks remain compatible with model context windows.

---

### Inputs

#### chunk_size (Integer)

##### Purpose

- Defines the maximum number of tokens allowed in a single chunk.

##### Example

chunk_size = 400

---

#### chunk_overlap (Integer)

##### Purpose

- Defines how many tokens should overlap between neighboring chunks.

- Helps preserve semantic continuity across chunk boundaries.

##### Example

chunk_overlap = 20

---

### Output

- A token-aware RecursiveCharacterTextSplitter object.

---

### When to Use

- During document ingestion.

- Before generating embeddings.

- Before storing chunks inside a vector database.

- When retrieval budgets are constrained by token limits rather than character counts.

---

### Example

splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=200,
    chunk_overlap=30
)

chunks = splitter.split_documents(raw_docs)

---

### Why Use This Instead of Character-Based Splitting?

Character count and token count are not equivalent.

Example:

text
100 characters

might become:

text
20 tokens

or

text
60 tokens

depending on the text.

Token-aware splitting guarantees that chunk sizes match actual LLM limits.

---

### Under the Hood

text
Raw Documents
       │
       ▼
Token-Aware Recursive Splitter
       │
       ▼
Paragraph Split
       │
       ▼
Sentence Split
       │
       ▼
Token Measurement
       │
       ▼
Chunk Size Validation
       │
       ▼
Final Chunks

---

## get_openai_callback()

### Purpose

- Provides a context manager that automatically tracks token usage and API cost.

- Intercepts OpenAI API calls executed within its scope.

- Records real usage statistics directly from the provider.

- Useful for auditing, debugging, and production monitoring.

---

### Inputs

None.

Used as a standard Python context manager.

---

### Output

- An OpenAICallbackHandler object.

After execution, the object contains:

- Prompt token count
- Completion token count
- Total token count
- Estimated API cost

---

### When to Use

- During production monitoring.

- When validating token budget calculations.

- When estimating operational costs.

- When debugging unexpectedly high API usage.

---

### Example

with get_openai_callback() as cb:
    response = chain.invoke("Your query here")

print(cb.prompt_tokens)
print(cb.completion_tokens)
print(cb.total_cost)

---

### Common Metrics Available

| Property | Description |
|-----------|-------------|
| prompt_tokens | Tokens sent to the model |
| completion_tokens | Tokens generated by the model |
| total_tokens | Sum of prompt and completion tokens |
| total_cost | Estimated API cost |

---

### Example Output

Prompt Tokens:      742
Completion Tokens: 183
Total Tokens:       925
Total Cost:         $0.0018

---

### Under the Hood

text
get_openai_callback()
           │
           ▼
      API Call
           │
           ▼
     Token Usage
           │
           ▼
 Cost Calculation
           │
           ▼
 Callback Object
           │
           ▼
 Usage Metrics

---

### Key Advantage

Without a callback:

estimated_tokens ≠ actual_tokens

With a callback:

actual_tokens = provider_reported_tokens

This makes the callback one of the most reliable tools for validating token budgets and monitoring production RAG systems.
## Field(description, enum, default)

### Purpose

Defines metadata, constraints, and descriptions for individual attributes within a Pydantic schema.

### Inputs

#### description (String)

Instructions telling the LLM what this specific data point is.

#### enum (List of Strings, Optional)

A strict list of allowed values.

#### default (Any, Optional)

The fallback value if the LLM cannot extract the data.

### Output

A Pydantic field configuration.

### When to use

When defining attributes inside your Pydantic class to ensure the LLM understands exactly what data to extract and is constrained to specific categories (e.g., locking a subject to only "General Physics" or "Linear Algebra").


---

## ChatOpenAI.with_structured_output(schema, method, include_raw)

### Purpose

Wraps the core language model to force it to return a structured Python object instead of a conversational string.

### Inputs

#### schema (Type[BaseModel] or Dict)

The Pydantic class or JSON schema you want the model to populate.

#### method (String, Optional)

The underlying API strategy (e.g., 'json_schema' or 'function_calling').

#### include_raw (Boolean, Optional)

Set to True if you want to see the model's raw response alongside the parsed data.

### Output

A LangChain Runnable that outputs a validated Pydantic object (or a dictionary).

### When to use

When transitioning from a chatbot to an agentic RAG-SLM system that needs to extract precise metadata tags from messy user queries.

---

## ChatPromptTemplate.from_messages(messages)

### Purpose

Constructs a structured prompt template by combining system instructions and dynamic human inputs.

### Inputs

#### messages (List of Tuples)

A list containing the roles and the prompt text.

### Output

A ChatPromptTemplate object that can be piped into an LLM.

### When to use

When you need to strictly separate your backend system instructions from the user's actual question.
