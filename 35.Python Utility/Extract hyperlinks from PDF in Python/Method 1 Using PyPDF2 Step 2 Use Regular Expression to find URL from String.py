# Import Module
import PyPDF2
import re

# Enter File Name
file = "Enter PDF File Name"

# Open File file
pdfFileObject = open(file, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)


# Regular Expression (Get URL from String)
def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(https?://\S+)"
    url = re.findall(regex, string)
    return [x for x in url]


# Iterate through all pages
for page_number in range(pdfReader.numPages):
    pageObject = pdfReader.getPage(page_number)

    # Extract text from page
    pdf_text = pageObject.extractText()

    # Print all URL
    print(Find(pdf_text))

# CLost the PDF
pdfFileObject.close()
