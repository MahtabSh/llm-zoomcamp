# Vector Search and Evaluation Project

## Overview

This project demonstrates how to leverage Elasticsearch for vector-based search and evaluates different retrieval methods. The main components of the project include:

1. **Introduction to Vector-Based Search**
2. **Ground Truth Generation for Evaluation**
3. **Text-Based Search Evaluation**
4. **Vector-Based Search Evaluation**

## Table of Contents

1. [Project Structure](#project-structure)
2. [Setup and Installation](#setup-and-installation)
3. [Usage](#usage)
4. [Evaluation](#evaluation)

## Project Structure

### 1. Introduction to Vector-Based Search

- **File**: `demo_es.ipynb`
- **Description**: This notebook introduces vector-based search using Elasticsearch. It covers:
  - Preparing documents and creating embeddings using pre-trained models.
  - Setting up an Elasticsearch index with vector fields.
  - Performing vector-based searches and hybrid queries combining vector and keyword searches.
  
### 2. Ground Truth Generation for Evaluation

- **File**: `ground_truth_generation.ipynb`
- **Description**: This notebook generates ground truth data for evaluation purposes. It includes:
  - Generating unique document IDs.
  - Formulating questions based on document content using OpenAI’s API.
  - Saving generated questions and associated data for later evaluation.

### 3. Text-Based Search Evaluation

- **File**: `evaluate-text.ipynb`
- **Description**: This notebook evaluates the performance of text-based search queries in Elasticsearch. It includes:
  - Implementing and running keyword-based searches.
  - Evaluating search performance using metrics such as Hit Rate and Mean Reciprocal Rank (MRR).

### 4. Vector-Based Search Evaluation

- **File**: `evaluate-vector.ipynb`
- **Description**: This notebook evaluates vector-based search capabilities using Elasticsearch. It covers:
  - Creating vector embeddings for different fields in the documents.
  - Implementing search functions for various vector queries.
  - Evaluating search results using metrics like Hit Rate and MRR for vector-based queries.

## Setup and Installation

1. **Install Required Packages**

   Install the necessary Python packages using pip:

   ```bash
   pip install elasticsearch pandas openai sentence-transformers transformers tqdm


## Usage

1. **Introduction to Vector-Based Search**

    Run the demo_es.ipynb notebook to learn about vector-based search and see practical examples of document indexing and querying in Elasticsearch. This notebook will guide you through:

    - Loading and preparing documents.
    - Creating embeddings using Sentence Transformers.
    - Setting up Elasticsearch with vector fields and performing vector-based searches.

2. **Ground Truth Generation**

    Execute the ground_truth_generation.ipynb notebook to create and save ground truth data. This involves:

    - Generating unique IDs for documents.
    - Using OpenAI’s API to generate questions from document content.
    - Saving the generated questions and relevant data to a CSV file.

3. **Text-Based Search Evaluation**

    Use the evaluate-text.ipynb notebook to perform and evaluate text-based searches. This includes:

    - Performing keyword-based searches in Elasticsearch.
    - Evaluating retrieval performance using Hit Rate and MRR metrics.

4. **Vector-Based Search Evaluation**

    Run the evaluate-vector.ipynb notebook to evaluate vector-based searches. This notebook covers:

    - Indexing documents with various vector embeddings.
    - Implementing search functions for different vector queries.
    - Evaluating search performance using Hit Rate and MRR metrics for vector-based queries.

## Evaluation

    The project evaluates search performance using the following metrics:

    - Hit Rate: Measures the proportion of queries for which at least one relevant document is retrieved.

    - Mean Reciprocal Rank (MRR): Measures the average rank at which the first relevant document is found.
    These metrics are applied to both text-based and vector-based search evaluations, providing a comprehensive assessment of retrieval performance.


