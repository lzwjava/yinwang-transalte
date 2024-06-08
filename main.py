import os
import boto3
import json

# Initialize a session using Amazon Bedrock
session = boto3.Session(region_name='us-east-1')

# Create Bedrock runtime client
bedrock_runtime = session.client('bedrock-runtime')


def translate_text(text):

    # Define the parameters for the invoke-model operation
    model_id = 'mistral.mixtral-8x7b-instruct-v0:1'

    body = {
        'prompt': 'Please translate below text to English:' + text,
        'max_tokens': 4096,
        'top_k': 10,
        'top_p': 0.7,
        'temperature': 0.7
    }

    response = bedrock_runtime.invoke_model(
        modelId=model_id,
        body=json.dumps(body),
        contentType='application/json'
    )

    output = json.loads(response['body'])

    return output


def read_and_translate(input_file, output_file):
    # Open the input file for reading and the output file for writing
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        # Read the content of the input file and split it into paragraphs
        paragraphs = infile.read().split('\n\n')

        # Group paragraphs into chunks of ten
        chunk_size = 10
        for i in range(0, len(paragraphs), chunk_size):
            chunk = paragraphs[i:i + chunk_size]

            # Concatenate paragraphs in the chunk
            chunk_text = '\n\n'.join(chunk)

            # Check if the chunk is not empty
            if chunk_text.strip():
                # Print the chunk for debugging purposes
                print(chunk_text)

                # Translate the chunk using the translate_text function
                translated_chunk = translate_text(chunk_text)

                # Write the translated chunk to the output file
                outfile.write(translated_chunk + '\n\n')


input_file = 'input.txt'
output_file = 'output.txt'

read_and_translate(input_file, output_file)
