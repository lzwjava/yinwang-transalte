import os
import json
import re


def load_urls(json_file):
    with open(json_file, 'r') as file:
        urls = json.load(file)
    return urls


def extract_date_and_slug(url):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/([^/]+)$', url)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        slug = match.group(4)
        return year, month, day, slug
    return None, None, None, None


def rename_files(directory, urls):
    for url in urls:
        year, month, day, slug = extract_date_and_slug(url)
        if year and month and day and slug:
            old_filename = f"{slug}.md"
            new_filename = f"{year}-{month}-{day}-{slug}.md"
            old_filepath = os.path.join(directory, old_filename)
            new_filepath = os.path.join(directory, new_filename)
            if os.path.exists(old_filepath):
                os.rename(old_filepath, new_filepath)
                print(f"Renamed: {old_filepath} -> {new_filepath}")
            else:
                print(f"File not found: {old_filepath}")


if __name__ == "__main__":
    json_file = 'yinwang.json'
    directory = 'translated_texts'
    urls = load_urls(json_file)
    rename_files(directory, urls)
