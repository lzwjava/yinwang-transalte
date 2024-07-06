import os
import boto3
import json


def translate_text(text):
    session = boto3.Session(region_name='us-east-1')
    bedrock_runtime = session.client('bedrock-runtime')

    model_id = 'meta.llama3-70b-instruct-v1:0'
    body = {
        'prompt': f'<s>[INST]Translate the following Chinese text to English, and provide only the English translation without any Chinese characters or punctuation: {text}[/INST]</s>',
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
        lines = []
        for line in infile:
            lines.append(line)
            if len(lines) == 10:
                text_to_translate = "".join(lines)
                translated_chunk = translate_text(text_to_translate)
                outfile.write(translated_chunk)
                lines = []

        # Translate any remaining lines
        if lines:
            text_to_translate = "\n".join(lines)
            translated_chunk = translate_text(text_to_translate)
            outfile.write(translated_chunk)


def translate_files_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.md'):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, filename)
            read_and_translate(input_file, output_file)
            print(f"Translated {input_file} to {output_file}")


input_directory = 'scraped_texts'
output_directory = 'translated_texts'

translate_files_in_directory(input_directory, output_directory)
