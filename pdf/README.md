# PDF Project

The `pdf-project` is a web application designed to provide a semantic search interface for PDF documents. Users can upload PDFs, perform semantic searches within these PDFs, and interact with an OpenAI language model (LLM) through a chat window to ask questions about the content of the PDFs.

## Features

- **PDF Upload**: Users can upload PDF documents to the application. The content of these documents is then indexed for semantic search.

- **Semantic Search**: Users can perform semantic searches within the uploaded PDFs. The search results are ranked based on their semantic relevance to the search query.

- **Chat Interface**: The application includes a chat window where users can converse with an LLM about the content of the PDFs. The LLM can answer questions, provide summaries, and offer insights based on the content of the PDFs.

- **Feedback Mechanism**: Users can provide feedback on the LLM's responses through a like/dislike system. This feedback can be used to improve the performance of the LLM over time.

# First Time Setup

## Using Pipenv [Recommended]

```
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db

```

## Using Venv [Optional]

These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv.

```
# Create the venv virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask --app app.web init-db
```

# Running the app [Pipenv]

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv devworker
```

### To run a local file-upload server.

- Go to the file_upload folder
- Install dependencies with `pip install -r requirements.txt`
- Start the server with `python app.py`
- In the `pdf` project, find the `.env` file and change the `UPLOAD_URL` line to the following: `UPLOAD_URL=http://localhost:8050`
- Restart the PDF project


### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
flask --app app.web init-db
```

# Running the app [Venv]

_These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv._

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
flask --app app.web init-db
```
