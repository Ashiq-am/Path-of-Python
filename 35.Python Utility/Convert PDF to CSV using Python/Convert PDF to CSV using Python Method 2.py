# Import Module
import tabula

# Read PDF File
# this contain a list
df = tabula.read_pdf(PDF_File_Path, pages = 1)[0] 

# Convert into Excel File
df.to_csv('Excel File Path')
