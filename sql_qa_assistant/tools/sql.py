import sqlite3
from typing import List

from langchain.tools import Tool
from pydantic.v1 import BaseModel

conn = sqlite3.connect('db.sqlite')


def run_sqlite_query(query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.OperationalError as err:
        return f'The following error occured: {str(err)}'


class RunQueryArgsSchema(BaseModel):
    query: str


def get_run_query_tool():
    return Tool(
        name='run_sqlite_query',
        description='Run a query on the sqlite database',
        func=run_sqlite_query,
        args_schema=RunQueryArgsSchema
    )


def list_tables():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cursor.fetchall()
    return '\n'.join(row[0] for row in rows if row[0] is not None)


def describe_tables(table_names):
    print('running describe tables')
    cursor = conn.cursor()
    tables_str = ', '.join(f"'{t}'" for t in table_names)
    print(tables_str)
    cursor.execute(
        "SELECT sql FROM sqlite_master WHERE type = 'table'"
        f" AND name IN ({tables_str});")
    rows = cursor.fetchall()
    return '\n'.join(row[0] for row in rows if row[0] is not None)


class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]


def get_describe_tables_tool():
    return Tool(
        name='describe_tables',
        description='Given a list of tables, return the list of '
        'columns in those tables',
        func=describe_tables,
        args_schema=DescribeTablesArgsSchema
    )
