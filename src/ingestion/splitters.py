import re
from typing import List
from langchain_text_splitters import TextSplitter

class CustomSplitter(TextSplitter):
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200, **kwargs):
        super().__init__(chunk_size=chunk_size, chunk_overlap=chunk_overlap, **kwargs)
        self.pattern = re.compile(
            r"(```.*?```|\$\$.*?\$\$|^#+\s.*?$)", 
            flags=re.DOTALL | re.MULTILINE
        )
        
    def split_text(self, text: str) -> List[str]:
        raw_splits = re.split(self.pattern, text)
        fragments = [s.strip() for s in raw_splits if s.strip()]
        return self._merge_splits(fragments, "\n\n")