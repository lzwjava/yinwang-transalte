import json
import requests
from bs4 import BeautifulSoup
import os
import re
import glob

# Load the URLs from the JSON file
with open('yinwang.json', 'r') as file:
    urls = json.load(file)

# Create a directory to save the scraped content
os.makedirs('scraped_texts', exist_ok=True)

files = glob.glob('scraped_texts/*')
for f in files:
    os.remove(f)


def html_to_markdown(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Convert header tags
    for i in range(1, 7):
        for tag in soup.find_all(f'h{i}'):
            header_text = tag.get_text(strip=True)
            markdown_header = f"{'#' * i} {header_text}"
            tag.insert_before(markdown_header + '\n')
            tag.decompose()

    # Convert <p> to new line
    for tag in soup.find_all('p'):
        tag.insert_before('\n' + tag.get_text(strip=True) + '\n')
        tag.decompose()

    # Convert <a> to [text](href)
    for tag in soup.find_all('a'):
        link_text = tag.get_text(strip=True)
        link_href = tag.get('href')
        tag.insert_before(f"[{link_text}]({link_href})")
        tag.decompose()

    # Convert <strong> and <b> to **text**
    for tag in soup.find_all(['strong', 'b']):
        strong_text = tag.get_text(strip=True)
        tag.insert_before(f"**{strong_text}**")
        tag.decompose()

    # Convert <em> and <i> to *text*
    for tag in soup.find_all(['em', 'i']):
        em_text = tag.get_text(strip=True)
        tag.insert_before(f"*{em_text}*")
        tag.decompose()

    # Convert lists
    for ul in soup.find_all('ul'):
        list_items = []
        for li in ul.find_all('li'):
            list_items.append(f"- {li.get_text(strip=True)}\n")
        ul.insert_before('\n'.join(list_items) + '\n')
        ul.decompose()

    for ol in soup.find_all('ol'):
        list_items = []
        for idx, li in enumerate(ol.find_all('li'), 1):
            list_items.append(f"{idx}. {li.get_text(strip=True)}\n")
        ol.insert_before('\n'.join(list_items) + '\n')
        ol.decompose()

    # Get the cleaned text
    markdown_text = soup.get_text(separator='\n')

    # Replace multiple newlines with exactly two newlines
    clean_markdown = re.sub(r'\n{2,}', '\n\n', markdown_text)

    return clean_markdown


def scrape_text_from_url(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        markdown_content = html_to_markdown(response.text)

        markdown_lines = markdown_content.split('\n')
        markdown_content = '\n'.join(markdown_lines[3:])

        return markdown_content
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return None


# Iterate over the URLs and scrape text
for index, url in enumerate(urls, start=1):
    print(f"Scraping {url}...")
    text = scrape_text_from_url(url)

    if text:
        # Save the text to a file
        filename = url.split('/')[-1] + '.md'

        filepath = os.path.join('scraped_texts', filename)

        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Saved to {filename}")
    else:
        print(f"Skipping {url} due to error.")

print("Scraping completed.")
