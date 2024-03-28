from typing import Any, Optional

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter

from app.chat.vector_stores.pinecone import pinecone_vs


class PDFIndexer:
    def __init__(
            self, text_splitter: Optional[TextSplitter] = None,
            loader: Optional[Any] = None
            ):
        if loader is None:
            self.loader = PyPDFLoader
        else:
            self.loader = loader

        if text_splitter is None:
            self.text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=100
            )
        else:
            self.text_splitter = text_splitter

    def __call__(self, pdf_id: str, pdf_path: str):
        """
        Index the specified PDF.

        1. Extract text from the specified PDF.
        2. Divide the extracted text into manageable chunks.
        3. Generate an embedding for each chunk.
        4. Persist the generated embeddings.

        :param pdf_id: The unique identifier for the PDF.
        :param pdf_path: The file path to the PDF.

        Example Usage:

        pdf_indexer = PDFIndexer()
        pdf_indexer('123456', '/path/to/pdf')
        """

        docs = self.loader(pdf_path).load_and_split(self.text_splitter)
        for doc in docs:
            doc.metadata = {
                "page": doc.metadata["page"],
                "text": doc.page_content,
                "pdf_id": pdf_id
            }
        pinecone_vs.add_documents(docs)
