import PyPDF2

file = "Enter PDF File Name"

pdfFileObject = open(file, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

for page_number in range(pdfReader.numPages):
    pageObject = pdfReader.getPage(page_number)
    pdf_text = pageObject.extractText()
    print(pdf_text)

pdfFileObject.close()
