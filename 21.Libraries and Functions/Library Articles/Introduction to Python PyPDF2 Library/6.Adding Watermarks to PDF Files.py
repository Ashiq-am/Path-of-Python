import PyPDF2

with open('example.pdf', 'rb') as main_pdf, open('watermark.pdf', 'rb') as watermark_pdf:
    reader = PyPDF2.PdfReader(main_pdf)
    watermark_reader = PyPDF2.PdfReader(watermark_pdf)

    writer = PyPDF2.PdfWriter()
    watermark_page = watermark_reader.pages[0]

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    # Save the watermarked PDF
    with open('watermarked.pdf', 'wb') as output_pdf:
        writer.write(output_pdf)
