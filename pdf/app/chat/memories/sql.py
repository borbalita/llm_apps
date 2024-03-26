from app.web.api import (
    add_message_to_conversation,
    get_messages_by_conversation_id,
)
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from pydantic import BaseModel


class SqlMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str

    @property
    def messages(self):
        return get_messages_by_conversation_id(self.conversation_id)

    def add_message(self, message: BaseMessage):
        add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content
        )

    def clear(self):
        pass


def build_memory(chat_args):
    return ConversationBufferMemory(
        chat_memory=SqlMessageHistory(
            conversation_id=chat_args.conversation_id),
        memory_key='chat_history',
        output_key='answer',
        return_messages=True
    )
