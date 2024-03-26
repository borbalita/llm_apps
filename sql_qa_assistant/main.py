from dotenv import load_dotenv
from handlers.chat_model import ChatModelStartHandler
from langchain.agents import AgentExecutor, OpenAIFunctionsAgent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from tools.report import get_write_report_tool
from tools.sql import get_describe_tables_tool, get_run_query_tool, list_tables

if __name__ == '__main__':
    load_dotenv()

    handler = ChatModelStartHandler()

    chat = ChatOpenAI(
        callbacks=[handler]
    )

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )

    tables = list_tables()

    prompt = ChatPromptTemplate(
        messages=[
            SystemMessage(
                content='You are an AI that has access to a SQLite database.'
                f' The following tables are available: {tables}.\n'
                'Do not make any assumptions about what columns exist in these'
                ' inside these tables. Instead, use the "describe_tables" tool.'
            ),
            # NOTE: add before human message!
            MessagesPlaceholder(variable_name='chat_history'),
            HumanMessagePromptTemplate.from_template('{input}'),
            MessagesPlaceholder(variable_name='agent_scratchpad'),
            # scratchpad
            # is a form of memory. it keeps track of intermittent (assistant)
            # messages and function results.
        ]
    )

    tools = [
        get_run_query_tool(),
        get_describe_tables_tool(),
        get_write_report_tool()
    ]

    agent = OpenAIFunctionsAgent(
        llm=chat,
        prompt=prompt,
        tools=tools
    )

    agent_executor = AgentExecutor(
        agent=agent,
        # verbose=True,
        tools=tools,
        memory=memory
    )

    agent_executor('How many orders are out there? '
                   'Please put the results into a report.')

    agent_executor('Now do the same for users.')
