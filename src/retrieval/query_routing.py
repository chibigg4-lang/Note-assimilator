from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field


class Queryrouting(BaseModel):
    reasoning: str = Field(description = 
                           "Think carefully and explain why you make that choice"
    )
    category:Literal["linear algebra", "Calculus", "Statistics", "Other"] = Field(
        description = 
        "Categorize the user's query into the correct academic domain.\n"
            "- 'Linear Algebra': Queries about matrices, vector spaces, SVD, eigenvalues, etc.\n"
            "- 'Calculus': Queries about gradients, multiple integrals, Green's Theorem, derivatives, etc.\n"
            "- 'Statistics': Queries about distributions, probabilities, variances, etc.\n"
            "- 'Other': Use this if the query is conversational, administrative, or unrelated to these three math domains."
    )
    keywords: list[str] = Field(
        default=[],
        description=(
                    "MUST include the exact core noun(s) from the user's query as the first items. "
                    "Then, generate 3-5 related mathematical concepts, full names of acronyms, or common alternate notations. "
                    "EXAMPLE 1: 'SVD' -> ['SVD', 'Singular Value Decomposition', 'matrix factorization', 'eigenvalues']. "
                    "EXAMPLE 2: 'Green's Theorem' -> ['Green's Theorem', 'line integral', 'double integral', 'vector field']. "
                    )
    )
    
    score: float = Field(
        ge = 0.0, le = 1.0, 
        description="A score between 0.0 and 1.0 indicating how certain you are that this is the correct route. 1.0 is absolute certainty."
    )
def classifying():
    llm = llm = ChatGoogleGenerativeAI(
        model = "gemini-3.1-flash-lite",
        temperature = 0.0,
        )
    classifier = llm.with_structured_output(Queryrouting)
    return classifier

