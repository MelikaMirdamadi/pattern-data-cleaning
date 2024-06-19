import json
import re

# Read the JSON content from the file
with open('input-path-file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def replace_newlines(obj):
    if isinstance(obj, str):
        # Replace multiple \n with a single n\
        return re.sub(r'\n{3,}', '\n\n', obj)

    elif isinstance(obj, list):
        # Recursively handle lists
        return [replace_newlines(item) for item in obj]
    elif isinstance(obj, dict):
        # Recursively handle dictionaries
        return {key: replace_newlines(value) for key, value in obj.items()}
    return obj

# Process the data to replace newlines
modified_data = replace_newlines(data)

# Write the modified JSON content back to the file
with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(modified_data, file, ensure_ascii=False, indent=4)

print("Newlines have been replaced successfully.")