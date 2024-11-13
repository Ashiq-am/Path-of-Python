# Import libraries
from Bio.SeqIO import parse

# file path/location
file = open('is_orchid.fasta')

# Parsing the FASTA file
for record in parse(file, "fasta"):
	print(record.id)
