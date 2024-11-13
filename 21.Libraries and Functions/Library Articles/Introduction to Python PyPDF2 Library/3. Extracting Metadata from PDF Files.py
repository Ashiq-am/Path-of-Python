import PyPDF2

with open('example.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    metadata = reader.metadata
    print(f"Author: {metadata.author}")
    print(f"Title: {metadata.title}")
    print(f"Creation Date: {metadata.creation_date}")
