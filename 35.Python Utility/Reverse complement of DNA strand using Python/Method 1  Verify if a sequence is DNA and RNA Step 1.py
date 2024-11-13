def verify(sequence):
    '''This code verfies if a sequence is a DNA or RNA'''
    # set the input sequence
    seq = set(sequence)

    # confirm if its elements is equal to the
    # set of valid DNA bases
    # Use a union method to ensure the sequence is
    # verified if does not conatin all the bases
    if seq == {"A", "T", "C", "G"}.union(seq):
        return "DNA"
    elif seq == {"A", "U", "C", "G"}.union(seq):
        return "RNA"
    else:
        return "Invalid sequence"


seq1 = "ATGCAGCTGTGTTACGCGAT"
seq2 = "UGGCGGAUAAGCGCA"
seq3 = "TYHGGHHHHH"

print(seq1 + " is " + verify(seq1))
print(seq2 + " is " + verify(seq2))
print(seq3 + " is " + verify(seq3))
