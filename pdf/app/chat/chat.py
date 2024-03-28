from langchain.chat_models import ChatOpenAI

from app.chat.chains.streamable import StreamableCRChain
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
    return StreamableCRChain.from_llm(
        llm=ChatOpenAI(streaming=chat_args.streaming),
        memory=sql_memory(chat_args),
        retriever=pinecone_retriever(chat_args),
        condense_question_llm=ChatOpenAI(streaming=False),
    )
