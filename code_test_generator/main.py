import argparse

from dotenv import load_dotenv
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


def _code_prompt():
    return PromptTemplate(
        template='Write a {language} function that will {task}.',
        input_variables=['language', 'task']
    )

def _test_prompt():
    return PromptTemplate(
        template='Write a test in {language} for the following {code}',
        input_variables=['language', 'code']
    )

def _get_llm():
    # The OpenAI API key should be stored in a .env file in the root directory of the project
    return OpenAI()


def _parse_args():
    parser = argparse.ArgumentParser(description='Solve a programming task in a given language')
    parser.add_argument('--language', type=str, help='programming language for the task', default='python')
    parser.add_argument('--task', type=str, help='task to be solved', default='add 1 and 2')
    return parser.parse_args()


if __name__ == '__main__':
    load_dotenv()
    args = _parse_args()
    
    code_chain = LLMChain(llm=_get_llm(), prompt=_code_prompt(), output_key='code')
    test_chain = LLMChain(llm=_get_llm(), prompt=_test_prompt(), output_key='test') 

    chain = SequentialChain(
        chains=[code_chain, test_chain],
        input_variables=['language', 'task'],
        output_variables=['code', 'test']
        )

    result = chain({'language': args.language, 'task': args.task})

    print('>>>>>>GENERATED CODE:')
    print(result['code'])
    
    print('>>>>>>GENERATED TEST:')
    print(result['test'])
