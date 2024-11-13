# Import libraries
from Bio import SeqIO

# Parsing file
filename = "sequence.fasta"
for record in SeqIO.parse(filename, "fasta"):

	# Showing records
	print("ID: %s" % record.id)
	print("Sequence length: %i" % len(record))
	print("Sequence description: %s" % record.description)
