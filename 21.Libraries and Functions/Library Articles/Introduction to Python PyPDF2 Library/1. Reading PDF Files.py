import PyPDF2

# Open a PDF file
with open('example.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")

    # Read the content of the first page
    first_page = reader.pages[0]
    text = first_page.extract_text()
    print(text)
