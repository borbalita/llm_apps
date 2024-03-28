from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory
from pydantic import BaseModel

from app.chat.models import ChatArgs
from app.web.api import (
    add_message_to_conversation,
    get_messages_by_conversation_id,
)


class SQLMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str

    @property
    def messages(self):
        return get_messages_by_conversation_id(self.conversation_id)

    def add_message(self, message):
        return add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content)

    def clear(str):
        pass


def sql_memory(chat_args: ChatArgs) -> ConversationBufferMemory:
    return ConversationBufferMemory(
        chat_memory=SQLMessageHistory(
            conversation_id=chat_args.conversation_id),
        return_messages=True,
        memory_key='chat_history',
        output_key='answer',
    )
