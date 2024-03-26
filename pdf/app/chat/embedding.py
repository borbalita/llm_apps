from typing import List, Optional

from app.chat.vectore_stores.pinecone import pinecone_vs
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter
from langchain.vectorstores import VectorStore
from langchain_core.documents import Document


def get_summary(docs: List[Document]) -> list[Document]:
    # Use a large context model like gpt-3.5-turbo-1106 (16k token)
    # or Anthropic Claude-2 (100k)
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo-1106')    
    chain = load_summarize_chain(llm, chain_type='stuff')
    summary = Document(page_content=chain.run(docs))
    summary.metadata['page'] = 'summary'
    return Document(page_content=summary)


class PDFEmbedder:

    def __init__(
        self,
        text_splitter: Optional[TextSplitter] = None,
        vectore_store: Optional[VectorStore] = None
    ):
        if text_splitter is None:
            self.text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=100
            )
        else:
            self.text_splitter = text_splitter
        if vectore_store is None:
            self.vector_store = pinecone_vs

    def __call__(self, pdf_id: str, pdf_path: str):
        """
        Generate and store embeddings for the given pdf

        1. Extract text from the specified PDF.
        2. Divide the extracted text into manageable chunks.
        3. Generate an embedding for each chunk.
        4. Persist the generated embeddings.

        :param pdf_id: The unique identifier for the PDF.
        :param pdf_path: The file path to the PDF.

        Example Usage:

        create_embeddings_for_pdf('123456', '/path/to/pdf')
        """
        loader = PyPDFLoader(pdf_path)
        docs = loader.load_and_split(self.text_splitter)
        docs.append(get_summary(docs))

        for doc in docs:
            doc.metadata = {
                'page': doc.metadata['page'],
                'text': doc.page_content,
                'pdf_id': pdf_id
            }

        self.vector_store.add_documents(docs)
