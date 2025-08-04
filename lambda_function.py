import boto3
import json
import logging

bedrock_agent = boto3.client('bedrock-agent-runtime', region_name='us-east-1')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Replace this with your actual Bedrock Knowledge Base ID
KNOWLEDGE_BASE_ID = 'KNOWLEDGE_BASE_ID_GOES_HERE'

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    user_message = event.get('message', '')
    if not user_message:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Missing 'message' in request"})
        }

    try:
        # Call retrieve_and_generate with proper parameter structure
        response = bedrock_agent.retrieve_and_generate(
            input={
                "text": user_message
            },
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": KNOWLEDGE_BASE_ID,
                    "modelArn": "anthropic.claude-v2:1"
                }
            }
        )

        generated_text = response.get('output', {}).get('text', '')

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "response": generated_text
        }

    except Exception as e:
        logger.error("Error querying knowledge base: %s", str(e))
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
