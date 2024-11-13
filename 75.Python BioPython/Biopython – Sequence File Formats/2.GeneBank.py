# Import libraries
from Bio import SeqIO
from Bio.SeqIO import parse

# Parsing Sequence
seq_record = next(parse(open('is_orchid.gbk'), 'genbank'))

# Sequence ID
print("\nSequence ID :", seq_record.id)

# Sequence Name
print("\nSequence Name :", seq_record.name)

# Sequence
print("\nSequence :", seq_record.seq)

# Sequence Description
print("\nSequence ID :", seq_record.description)

# Sequence Annotations
print("\nSequence Annotations :", seq_record.annotations)
