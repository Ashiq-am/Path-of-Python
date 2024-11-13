# Import Module
import pdfx

# Read PDF File
pdf = pdfx.PDFx("File Name")

# Get list of URL
print(pdf.get_references_as_dict())
