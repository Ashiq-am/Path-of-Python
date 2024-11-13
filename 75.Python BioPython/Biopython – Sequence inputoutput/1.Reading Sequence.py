# Import libraries
from Bio import SeqIO

# Reading file
record = SeqIO.read("sequence.gb", "genbank")

# Showing records
print("ID: %s" % record.id)
print("Sequence length: %i" % len(record))
print("Sequence description: %s" % record.description)
