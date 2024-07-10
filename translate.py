import os
import requests
from bs4 import BeautifulSoup, NavigableString
import boto3
import json
import re


def contains_chinese(text):
    return bool(re.search(r'[\u4e00-\u9fff]', text))


def translate_text(text):
    session = boto3.Session(region_name='us-east-1')
    bedrock_runtime = session.client('bedrock-runtime')

    model_id = 'meta.llama3-70b-instruct-v1:0'
    body = {
        'prompt': f'<s>[INST]Translate the following Chinese text to English, and provide only the English translation: {text}[/INST]</s>'
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
    extracted_text = output['generation']
    return extracted_text


def translate_html_recursively(element):
    if isinstance(element, NavigableString):
        if contains_chinese(element):
            translated_text = translate_text(str(element))
            return NavigableString(translated_text)
        return element

    for idx, child in enumerate(element.contents):
        if isinstance(child, NavigableString):
            if contains_chinese(child):
                translated_text = translate_text(str(child))
                element.contents[idx] = NavigableString(translated_text)
        elif hasattr(child, 'contents'):
            translate_html_recursively(child)
    return element


def scrape_html_from_url(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Get the raw HTML content
        html_content = response.text

        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return None


def translate_url_to_text(url, output_file):
    print(f"Scraping {url}...")
    html = scrape_html_from_url(url)

    if html:
        print("Translating HTML...")
        soup = BeautifulSoup(html, 'html.parser')
        translated_soup = translate_html_recursively(soup)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(str(translated_soup))
        print(f"Saved translated HTML to {output_file}")
    else:
        print(f"Skipping {url} due to error.")


def main():
    with open('yinwang.json', 'r') as file:
        urls = json.load(file)

    output_dir = 'translated_html'
    os.makedirs(output_dir, exist_ok=True)

    for url in urls:
        output_file = os.path.join(output_dir, f"{os.path.basename(url)}.html")
        translate_url_to_text(url, output_file)


if __name__ == "__main__":
    main()
