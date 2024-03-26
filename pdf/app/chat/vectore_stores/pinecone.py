import os

import pinecone
from app.chat.embeddings.openai import embeddings
from app.chat.models import ChatArgs
from langchain.vectorstores.pinecone import Pinecone

pinecone.init(
    api_key=os.getenv('PINECONE_API_KEY'),
    environment=os.getenv('PINECONE_ENV_NAME')
)

pinecone_vs = Pinecone.from_existing_index(
    os.getenv('PINECONE_INDEX_NAME'),
    embeddings
)


def build_retriever(chat_args: ChatArgs):
    if chat_args.pdf_id is None:
        search_kwargs = {'filter': {'page': 'summary'}}
    else:
        search_kwargs = {'filter': {'pdf_id': chat_args.pdf_id}}

    return pinecone_vs.as_retriever(search_kwargs=search_kwargs)
