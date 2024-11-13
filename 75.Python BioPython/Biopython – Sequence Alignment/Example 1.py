# Import libraries
from Bio import AlignIO

# Creating Sequence Alignment
alignment = AlignIO.read(open("PF18225_seed.txt"), "stockholm")

# Print alignment object
print(alignment)

# Show alignment sequence record
print("Showing Alignment Sequence Record")
for align in alignment:
	print(align.seq)
