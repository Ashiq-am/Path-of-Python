# Importing our library and reading the doc file
import docx
doc = docx.Document('csv/g.docx')

# Printing the title
print(doc.paragraphs[0].text)
