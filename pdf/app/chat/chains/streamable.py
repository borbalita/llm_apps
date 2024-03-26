from queue import Queue
from threading import Thread

from app.chat.callbacks.stream import StreamingHandler
from langchain.chains import ConversationalRetrievalChain


class StreamableChainMixin:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task():
            self(input, callbacks=[handler])

        Thread(target=task).start()

        while True:
            token = queue.get()
            if token is None:
                break

            yield token


class StreamingConversationalRetrievalChain(
        StreamableChainMixin, ConversationalRetrievalChain):
    pass
