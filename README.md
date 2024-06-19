
---

# Pattern Data Cleaning Tool

This Python script reads a JSON file, processes its content to replace multiple consecutive newlines with a single newline, and writes the cleaned content back to a new JSON file. This tool is useful for cleaning up text data in JSON files that contain unnecessary newline characters.

## Features

- Reads JSON content from a specified input file.
- Replaces multiple consecutive newline characters with a single newline.
- Handles nested structures within the JSON, such as lists and dictionaries.
- Writes the cleaned JSON content to a specified output file.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MelikaMirdamadi/pattern-data-cleaning.git
   cd pattern-data-cleaning
   ```

2. **Ensure you have Python installed:**

   This script requires Python 3. Make sure Python is installed on your system.

3. **Install required packages:**

   This script uses the `json` and `re` modules from the Python Standard Library, so no additional packages are required.

## Usage

1. **Prepare your input JSON file:**

   Ensure you have an input JSON file named `input-path-file.json` in the same directory as the script. This file should contain the JSON content you want to clean.

2. **Run the script:**

   Execute the script using Python:

   ```bash
   python clean_newlines.py
   ```

3. **Output:**

   The cleaned JSON content will be written to a file named `output.json` in the same directory. A message "Newlines have been replaced successfully." will be printed to the console upon successful execution.

## Example

Given an input JSON file (`input-path-file.json`):

```json
{
    "text": "This is some text.\n\n\nThis is more text with multiple newlines."
}
```

After running the script, the output JSON file (`output.json`) will be:

```json
{
    "text": "This is some text.\n\nThis is more text with multiple newlines."
}
```

## Customization

- If you want to change the input or output file paths, you can modify the following lines in the script:

  ```python
  with open('input-path-file.json', 'r', encoding='utf-8') as file:
      data = json.load(file)

  # ...

  with open('output.json', 'w', encoding='utf-8') as file:
      json.dump(modified_data, file, ensure_ascii=False, indent=4)
  ```

## Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

