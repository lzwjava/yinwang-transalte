import os
import boto3
import json


def translate_text(text):
    session = boto3.Session(region_name='us-east-1')
    bedrock_runtime = session.client('bedrock-runtime')

    model_id = 'mistral.mixtral-8x7b-instruct-v0:1'
    body = {
        'prompt':  f'Translate the following Chinese text to English: {text}',
        'max_tokens': 4096,
        'top_k': 50,
        'top_p': 0.7,
        'temperature': 0.7
    }

    response = bedrock_runtime.invoke_model(
        modelId=model_id,
        body=json.dumps(body),
        contentType='application/json'
    )

    # Read the content from the StreamingBody
    response_body = response['body'].read().decode('utf-8')
    output = json.loads(response_body)

    # Extract the text from the response
    extracted_text = output['outputs'][0]['text']
    return extracted_text


def read_and_translate(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        chunk_size = 1024
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break
            print(chunk)
            translated_chunk = translate_text(chunk)
            outfile.write(translated_chunk + '\n')


input_file = 'input.txt'
output_file = 'output.txt'

read_and_translate(input_file, output_file)
