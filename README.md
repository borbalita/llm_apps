# Repository for LLM based applications

The `llm_apps` project is a collection of applications that leverage the capabilities of OpenAI's language models. Each subproject within `llm_apps` focuses on a specific use case or application of these models.

## Subprojects

### SQL QA Assistant

The `sql-qa-assistant` subproject provides a Question-Answering (QA) interface to interact with SQL databases. It uses an OpenAI language model to interpret natural language queries, translate them into SQL queries, and execute them against a specified SQL database.

### Code Test Generator

The `code-test-generator` subproject generates code snippets and corresponding tests based on user-provided tasks and programming languages. It uses an OpenAI language model to generate the code and tests.

### PDF Project

The `pdf-project` subproject is a web application designed to provide a semantic search interface for PDF documents. Users can upload PDFs, perform semantic searches within these PDFs, and interact with an OpenAI language model (LLM) through a chat window to ask questions about the content of the PDFs.

## Getting Started

To get started with `llm_apps`, clone the repository and navigate to the subproject you're interested in.

```bash
git clone https://github.com/yourusername/llm_apps.git
cd llm_apps/sql-qa-assistant