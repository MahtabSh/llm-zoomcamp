import streamlit as st
import time
from elasticsearch import Elasticsearch
from openai import OpenAI

# Initialize OpenAI and Elasticsearch clients
client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama'
)
es_client = Elasticsearch('http://localhost:9200')

def elastic_search(query, index_name="course-questions"):
    """
    Perform a search query on the Elasticsearch index.

    Args:
    query (str): The query string to search for.
    index_name (str): The name of the Elasticsearch index.

    Returns:
    list: A list of search results documents.
    """
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        }
    }
    response = es_client.search(index=index_name, body=search_query)
    
    result_docs = []
    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])
    
    return result_docs

def build_prompt(query, search_results):
    """
    Build a prompt for the language model based on search results.

    Args:
    query (str): The user's query.
    search_results (list): A list of search results documents.

    Returns:
    str: A formatted prompt string.
    """
    prompt_template = """
    You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
    Use only the facts from the CONTEXT when answering the QUESTION.

    QUESTION: {question}

    CONTEXT: 
    {context}
    """.strip()
    
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt):
    """
    Generate a response from the language model based on the prompt.

    Args:
    prompt (str): The prompt string to send to the language model.

    Returns:
    str: The language model's response.
    """
    response = client.chat.completions.create(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

def rag(query):
    """
    Perform a Retrieval-Augmented Generation (RAG) query.

    Args:
    query (str): The user's query.

    Returns:
    str: The generated answer from the language model.
    """
    search_results = elastic_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer

def main():
    """
    Streamlit application main function to handle user inputs and display the RAG-generated answers.
    """
    st.title("RAG Function Invocation")

    user_inputs = st.text_input("Enter your input:")

    if st.button("Ask"):
        with st.spinner('Processing ...'):
            output = rag(user_inputs)
            st.success("completed")
            st.write(output)

if __name__ == "__main__":
    main()
