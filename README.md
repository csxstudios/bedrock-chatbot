# bedrock-chatbot
Simple RAG chatbot using a Bedrock Knowledge Base w/ an S3 vector store

## Solution Overview
1. S3 Bucket Setup
    - Create an S3 bucket to store knowledge base documents
    - Upload documents
2. Bedrock Setup
    - Modify model access to include Titan Text Embeddings V2 and Claude
    - Create a Knowledge Base pointed to above S3 bucket and choose S3 vector store (preview)
    - Once datasource is created, make sure to "Sync"
3. Lambda Function:
    - Create a lambda function that sends chat questions and history to query the Bedrock Knowledge Base
4. API Gateway Setup
    - Create an API using Amazon API Gateway w/ a POST method to trigger the above lambda function

