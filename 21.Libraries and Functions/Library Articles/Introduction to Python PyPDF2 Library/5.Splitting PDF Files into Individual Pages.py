import PyPDF2

with open('merged.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    for i, page in enumerate(reader.pages):
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)

        # Save each page as a new file
        with open(f'page_{i+1}.pdf', 'wb') as output_pdf:
            writer.write(output_pdf)
