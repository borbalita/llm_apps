from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from app.chat.memories.sql_memory import sql_memory
from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecone import pinecone_retriever


def build_chat(chat_args: ChatArgs):
    """
    :param chat_args: ChatArgs object containing
        conversation_id, pdf_id, metadata, and streaming flag.

    :return: A chain

    Example Usage:

        chain = build_chat(chat_args)
    """
    return ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(),
        memory=sql_memory(chat_args),
        retriever=pinecone_retriever(chat_args),
    )
