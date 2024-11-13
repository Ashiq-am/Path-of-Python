# Import docx NOT python-docx
import docx

# Create an instance of a word document
doc = docx.Document()

# Selecting a section of the document
section = doc.sections[0]

# Printing the default orientation.
print("Default Orientation:", section.orientation)
