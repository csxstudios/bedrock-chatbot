# bedrock-chatbot
Simple RAG chatbot using a Bedrock Knowledge Base w/ an S3 vector store

## Solution Overview
1. S3 Bucket Setup
    - Create an S3 bucket to store knowledge base documents
    - Upload documents
2. Bedrock Setup
    - Modify model access to include Titan Text Embeddings V2 and Claude
    - Create a Knowledge Base pointed to the above S3 bucket and choose S3 vector store (preview)[^1]
    - Once datasource is created, make sure to "Sync"
3. Lambda Function:
    - Create a lambda function that sends chat questions and history to query the Bedrock Knowledge Base
4. API Gateway Setup
    - Create an API using Amazon API Gateway w/ a POST method to trigger the above lambda function
    - Secure the API by requiring an API key

*[^1]: Bedrock Knowledge Base's typically use OpenSearch Serverless for its vectore store, which is NOT pay-per-use. The OpenSearch Serverless service is charged at $0.24/hr for 2 OCUs at a minimum. This equates to $11.52/day or $4,204.80/year. As an alternative, S3 vectors preview is available with a reported 90% cost savings.*

## Architecture
![alt text](https://github.com/csxstudios/bedrock-chatbot/blob/main/bedrock-chatbot-architecture.png?raw=true)