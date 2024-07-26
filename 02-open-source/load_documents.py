import json
from elasticsearch import Elasticsearch


# Load the raw documents from the JSON file
with open('documents.json', 'rt') as f_in:
    docs_raw = json.load(f_in)

documents = []

# Extract and format documents for indexing
for course_dict in docs_raw:
    for doc in course_dict['documents']:
        doc['course'] = course_dict['course']
        documents.append(doc)

# Initialize the Elasticsearch client
es_client = Elasticsearch('http://localhost:9200')

# Define the index settings and mappings
index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"} 
        }
    }
}

index_name = "course-questions"

# Create the Elasticsearch index with the defined settings
es_client.indices.create(index=index_name, body=index_settings)

# Index each document into the Elasticsearch index
for doc in documents:
    es_client.index(index=index_name, document=doc)