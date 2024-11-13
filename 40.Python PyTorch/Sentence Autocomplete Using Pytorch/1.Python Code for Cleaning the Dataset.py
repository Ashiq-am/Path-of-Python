import re
import string
import torch
import pandas as pd
from docx import Document

# Read the DOCX file
doc_path = "wikipedia.docx"
doc = Document(doc_path)

# Extract text from paragraphs
text_data = [paragraph.text for paragraph in doc.paragraphs]

# Convert text to lowercase
text_data =

# Remove special characters and words between them using regex
text_data = [re.sub(r"\[.*?\]", "", text) for text in text_data]

# Remove words not in the English alphabet
english_alphabet = set(string.ascii_lowercase)
text_data = [' '.join([word for word in text.split()\
					if all(char in english_alphabet\
							for char in word)]) for text in text_data]

# Remove leading/trailing whitespaces
text_data =

# Remove empty sentences
text_data =

# Create a DataFrame with the cleaned text data
df = pd.DataFrame({"Text": text_data})

# Save the cleaned text data to a CSV file
output_path = "output.csv"
# Set index=False to exclude the index column in the output
df.to_csv(output_path, index=False)

print("Text data cleaned and saved to:", output_path)
