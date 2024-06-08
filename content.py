import os


def strip_left_spaces(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Counter for the first three non-empty lines
    non_empty_line_count = 0
    processed_lines = []

    for line in lines:
        # Strip leading spaces from the first three non-empty lines
        if non_empty_line_count < 5 and line.strip():
            processed_lines.append(line.lstrip())
            non_empty_line_count += 1
        else:
            processed_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)


def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            strip_left_spaces(file_path)
            print(f"Processed: {file_path}")


if __name__ == "__main__":
    directory = 'translated_texts'
    process_directory(directory)
