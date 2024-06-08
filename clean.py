import os
import re


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if len(lines) > 0 and len(lines[0].strip()) > 0:
        first_line = lines[0].strip()
        if len(first_line) < 50 and not first_line.endswith('.'):
            title = first_line
            content_start = 1
        else:
            # Use filename without date as title
            filename = os.path.splitext(os.path.basename(file_path))[0]
            # Remove date from the filename
            title = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
            content_start = 0
    else:
        # Use filename without date as title
        filename = os.path.splitext(os.path.basename(file_path))[0]
        title = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename)
        content_start = 0

    # Remove ": " if present at the start of the title
    if title.startswith(": "):
        title = title[2:]

    jekyll_content = f"""---
layout: post
title: "{title}"
---

""" + "".join(lines[content_start:])

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(jekyll_content)


def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            process_file(file_path)
            print(f"Processed: {file_path}")


if __name__ == "__main__":
    directory = 'translated_texts'
    process_directory(directory)
