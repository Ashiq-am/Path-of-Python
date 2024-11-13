# Import libraries
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.pairwise2 import format_alignment

# Creating sqmple sequences
seq1 = Seq("TGTGACTA")
seq2 = Seq("CATGGTCA")

# Finding similarities
alignments = pairwise2.align.globalxx(seq1, seq2)

# Showing results
for alignment in alignments:
	print(format_alignment(*alignment))
