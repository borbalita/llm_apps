from queue import Queue
from threading import Thread
from typing import Optional

from flask import current_app
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import ConversationalRetrievalChain


class StreamingHandler(BaseCallbackHandler):
    def __init__(self, queue: Queue):
        self.queue = queue
        self.streaming_run_ids = set()

    def on_chat_model_start(self, serialized, messages, run_id, **kwargs
                            ) -> None:
        if serialized['kwargs']['streaming']:
            self.streaming_run_ids.add(run_id)

    def on_llm_new_token(self, token: str, run_id, **kwargs) -> None:
        if run_id in self.streaming_run_ids:
            self.queue.put(token)

    def on_llm_end(self, response: str, run_id, **kwargs) -> None:
        if run_id in self.streaming_run_ids:
            self.queue.put(None)
            self.streaming_run_ids.remove(run_id)

    def on_llm_error(self, error: Optional[str], run_id, **kwargs) -> None:
        if run_id in self.streaming_run_ids:
            self.queue.put(None)
            self.streaming_run_ids.remove(run_id)


class StreamableChainMixin:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler])

        Thread(target=task, args=[current_app.app_context()]).start()

        while True:
            token = queue.get()
            if token is None:
                break

            yield token


class StreamableCRChain(StreamableChainMixin, ConversationalRetrievalChain):
    pass
