# RAG-Based FAQ System

This project is a Retrieval-Augmented Generation (RAG) based FAQ system that uses Elasticsearch for document retrieval and OpenAI's language model for generating answers.

## Project Structure

- `load_documents.py`: Script to load documents from a JSON file and index them into Elasticsearch.
- `qa_faq.py`: Streamlit application to perform RAG queries and display the answers.
- `docker-compose.yml`: Docker Compose file to set up Elasticsearch and Ollama services.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Step-by-Step Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/MahtabSh/llm-zoomcamp.git
    cd llm-zoomcamp/02-open-source/
    ```

2. **Set up the services using Docker Compose**:

    ```bash
    docker-compose up -d
    ```

4. **Install the phi3 model in Ollama**:

    First, enter the Ollama container:

    ```bash
    docker exec -it ollama bash
    ```

    Then, pull the phi3 model:

    ```bash
    ollama pull phi3
    ```

5. **Index the documents**:

    Place your `documents.json` file in the same directory as `load_documents.py` and run:

    ```bash
    python load_documents.py
    ```

6. **Run the Streamlit application**:

    ```bash
    streamlit run qa_faq.py
    ```

## Usage

- Open your web browser and go to `http://localhost:8501`.
- Enter your query in the text input box and click "Ask".
- The application will display the generated answer based on the indexed documents.

## Files

### `load_documents.py`

This script reads documents from a JSON file and indexes them into an Elasticsearch instance. It processes the JSON data to extract documents, associating each document with its course, and creates an index in Elasticsearch with the specified settings and mappings.

### `qa_faq.py`

This Streamlit application performs RAG queries. It sends a user's query to Elasticsearch, constructs a prompt for the language model based on the search results, and retrieves the generated response from the language model.

### `docker-compose.yml`

This Docker Compose file sets up Elasticsearch and Ollama services. It defines the settings for running Elasticsearch as a single-node cluster and maps the necessary ports to the host machine.

