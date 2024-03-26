# SQL QA Assistant

The `sql-qa-assistant` project provides a Question-Answering (QA) interface to interact with SQL databases. The `main.py` script is the entry point of the application.

## Description

The `main.py` script in the `sql-qa-assistant` module uses an OpenAI language model to interpret natural language queries and translate them into SQL queries. It then executes these queries against a specified SQL database and returns the results.

The script uses a set of tools, including `get_run_query_tool()`, `get_describe_tables_tool()`, and `get_write_report_tool()`, to interact with the database. The `OpenAIFunctionsAgent` and `AgentExecutor` classes are used to manage the interaction between the language model, the tools, and the database.

## TBC

The project is to be extended to provide a terminal chat interface to interact with the SQL database and generate reports.