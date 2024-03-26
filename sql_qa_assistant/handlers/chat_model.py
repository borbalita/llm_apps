from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))


def _get_message_color(message):
    if message.type == 'system':
        return 'yellow'
    elif message.type == 'human':
        return 'green'
    elif message.type == 'ai' and 'function_call' in message.additional_kwargs:
        return 'red'
    elif message.type == 'ai':
        return 'blue'
    elif message.type == 'function':
        return 'purple'
    else:
        return 'white'


def _get_text(message):
    if message.type == 'ai' and 'function_call' in message.additional_kwargs:
        call = message.additional_kwargs['function_call']
        return f"Running tool {call['name']} with args {call['arguments']}"
    else:
        return message.content


class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, **kwargs):
        # NOTE: assume that no batching used => len(messages) == 1
        print("\n\n\n\n========= Sending Messages to ChatGPT =========\n\n\n\n")

        for message in messages[0]:
            boxen_print(
                _get_text(message),
                title=message.type,
                color=_get_message_color(message)
            )
