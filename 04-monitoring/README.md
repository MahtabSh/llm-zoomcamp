### 1. Offline RAG Evaluation
    This project focuses on evaluating the performance of a Retrieval-Augmented Generation (RAG) system using Elasticsearch. The RAG approach enhances the capabilities of generative models by incorporating relevant information retrieved from a document corpus, making it particularly useful in scenarios where the model needs to answer questions based on external knowledge.

- **File**: `offline-rag-evaluation.ipynb`
- **Description**: This notebook is designed to evaluate the retrieval component of a RAG system in an offline environment. It includes:
  - Setting up an Elasticsearch index to store and search the document corpus.
  - Configuring the index with vector-based search capabilities using dense vectors.
  - Populating the index with documents that include questions, sections, text, and their respective vector embeddings.
  - Performing retrieval evaluations based on the cosine similarity of vector representations.
  - Performing retrival evaluations based on the LLM-as-a-Judge

### 2. Course Assistant App

## Project Overview

This project is a Course Assistant application that leverages various AI models and Elasticsearch to answer user queries related to different courses. It includes a web interface built using Streamlit, a backend with database management, and an AI-driven question-answering system.

## Features

- **Course Selection:** Users can choose between different courses, including "Machine Learning Zoomcamp", "Data Engineering Zoomcamp", and "MLOps Zoomcamp".
- **Model Selection:** Users can select different models for generating answers.
- **Search Type:** Supports both text-based and vector-based search using Elasticsearch.
- **Real-time Feedback:** Users can provide feedback on the generated answers, which is stored in the database.
- **Historical Data Generation:** The project includes functionality for generating synthetic historical data for testing.

## Project Structure

```plaintext
├── app.py                   # Streamlit application entry point
├── assistant.py             # Core logic for handling queries and interacting with AI models
├── db.py                    # Database operations (PostgreSQL)
├── prep.py                  # Script for preparing and indexing documents in Elasticsearch
├── generate_data.py         # Script for generating synthetic and live data
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
└── README.md                # Project documentation


## File Descriptions
- **app.py**: The main Streamlit app where users interact with the Course Assistant.
- **assistant.py**: Contains the logic for querying Elasticsearch, generating prompts, and interacting with the AI models.
- **db.py**: Manages database connections and operations, including saving conversations and feedback.
- **prep.py**: Prepares data and sets up Elasticsearch indices for vector-based search.
- **generate_data.py**: Generates synthetic historical data and simulates live data for testing and development purposes.

## Setup Instructions
**Prerequisites**
- Python 3.8+
- PostgreSQL
- Elasticsearch
- Streamlit

## Installation
    1. Clone the repository:
        git clone https://github.com/yourusername/course-assistant.git
        cd course-assistant
    2. Set up a virtual environment:
       python -m venv venv
       source venv/bin/activate  
    3. Install the dependencies:
       pip install -r requirements.txt
    4. Set up PostgreSQL:
        Create a database named course_assistant.
    5. Set up Elasticsearch:
        Ensure Elasticsearch is running locally or accessible.
        Run the prep.py script to set up indices and load data into Elasticsearch:
           python prep.py
## Usage
    1. Run the Streamlit application:
    streamlit run app.py
    2. Interact with the application:
        - Select a course, choose a model, and type in your question.
        - The assistant will provide an answer based on the selected options.
        - You can provide feedback on the relevance of the answer, which will be stored in the database.
    3. Generate Synthetic Data:
    To generate historical and live data for testing, run:
        python generate_data.py







        



