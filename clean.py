import os


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if len(lines) > 0 and len(lines[0].strip()) > 0:
        title = lines[0].strip()
        content_start = 1
    else:
        title = os.path.splitext(os.path.basename(file_path))[0]
        content_start = 0

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
