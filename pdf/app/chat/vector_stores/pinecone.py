import os

import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone

from app.chat.models import ChatArgs

pinecone.init(
    api_key=os.getenv('PINECONE_API_KEY'),
    environment=os.getenv('PINECONE_ENV_NAME'),
)

pinecone_vs = Pinecone.from_existing_index(
    os.getenv('PINECONE_INDEX_NAME'),
    OpenAIEmbeddings(),
)


def pinecone_retriever(chat_args: ChatArgs):
    search_kwargs = {'filter': {'pdf_id': chat_args.pdf_id}}
    return pinecone_vs.as_retriever(search_kwargs=search_kwargs)
