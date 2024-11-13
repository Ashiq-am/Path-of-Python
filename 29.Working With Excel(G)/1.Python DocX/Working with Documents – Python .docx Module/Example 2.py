# Import docx NOT python-docx
import docx

# Opening a previously created document
doc = docx.Document('gfg.docx')

# Now save the document to a location
doc.save('gfg-copy.docx')
