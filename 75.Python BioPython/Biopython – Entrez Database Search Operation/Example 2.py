# Import libraries
from Bio import Entrez

# Setting email
Entrez.email = 'jeetesh1@yopmail.com'

# Setting Entrez tool parameter
Entrez.tool = 'Demoscript'

# Searching for database
info = Entrez.egquery(term="genome")

record = Entrez.read(info)
for row in record["eGQueryResult"]:
	print(row["DbName"], row["Count"])
