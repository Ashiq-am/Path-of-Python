# Import docx NOT python-docx
import docx
from docx.enum.section import WD_ORIENT

# Create an instance of a word document
doc = docx.Document()

# Selecting a section of the document
section = doc.sections[0]

# Printing the default orientation.
print("Default Orientation:",
	section.orientation)

# Changing the orientation to landscape
section.orientation = WD_ORIENT.LANDSCAPE

# Printing the new orientation.
print("New Orientation:",
	section.orientation)
