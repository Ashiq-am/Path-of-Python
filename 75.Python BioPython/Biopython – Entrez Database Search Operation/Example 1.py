# Import libraries
from Bio import Entrez

# Setting email
Entrez.email = 'jeetesh1@yopmail.com'

# Setting Entrez tool parameter
Entrez.tool = 'Demoscript'

# Searching for database
info = Entrez.esearch(db="nucleotide", term="genome")

# reading records
record = Entrez.read(info)

# Showing records
print(record)
