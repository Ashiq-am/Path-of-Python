import PyPDF2

with open('example.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:
        print(page.extract_text())
