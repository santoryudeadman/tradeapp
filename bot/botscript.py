import re

def preprocess_text(input_text):
    # Replace line breaks and extra whitespace with a single space
    input_text = re.sub(r'[\n\r]+', ' ', input_text)
    input_text = re.sub(r'\s+', ' ', input_text)

    # Replace double quotes with single quotes
    input_text = re.sub(r'"', "'", input_text)

    # Add periods to sentences without ending punctuation
    input_text = re.sub(r'(?<=[a-z])\n(?=[A-Z])', '. ', input_text)
    input_text = re.sub(r'(?<=[a-z])\n(?=[^A-Za-z])', '. ', input_text)
    input_text = re.sub(r'(?<=[a-z])(?<![mr])\n(?=$|\n)', '. ', input_text)

    # Replace bullet points with dashes
    input_text = re.sub(r'\n?•\s', '- ', input_text)

    # Add spaces after punctuation and remove spaces before punctuation
    input_text = re.sub(r'\s([.,:;?!])\s', r' \1 ', input_text)

    # Convert to lowercase
    input_text = input_text.lower()

    return input_text

# Read the input file
with open('Corpus_v2.2.txt', 'r') as f:
    input_text = f.read()

# Preprocess the input text
converted_text = preprocess_text(input_text)

# Write the transformed text to a new file
with open('converted.txt', 'w') as f:
    f.write(converted_text)
