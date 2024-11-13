def verify(sequence):
    '''This code verfies if a sequence is a DNA or RNA'''

    # set the input sequence
    seq = set(sequence)

    # confirm if its elements is equal to
    # the set of valid DNA bases
    # Use a union method to ensure the
    # sequence is verified if does not
    # conatin all the bases
    if seq == {"A", "T", "C", "G"}.union(seq):
        return "DNA"
    elif seq == {"A", "U", "C", "G"}.union(seq):
        return "RNA"
    else:
        return "Invalid sequence"


def rev_comp_if(seq):
    comp = []
    if verify(seq) == "DNA":
        for base in seq:
            if base == "A":
                comp.append("T")
            elif base == "G":
                comp.append("C")
            elif base == "T":
                comp.append("A")
            elif base == "C":
                comp.append("G")
    elif verify(seq) == "RNA":
        for base in seq:
            if base == "U":
                comp.append("A")
            elif base == "G":
                comp.append("C")
            elif base == "A":
                comp.append("U")
            elif base == "C":
                comp.append("G")
    else:
        return "Invalid Sequence"

    # reverse the sequence
    comp_rev = comp[::-1]

    # convert list to string
    comp_rev = "".join(comp_rev)
    return comp_rev


seq1 = "ATGCAGCTGTGTTACGCGAT"
seq2 = "UGGCGGAUAAGCGCA"
seq3 = "TYHGGHHHHH"

print("The reverse complementary strand of " +
      seq1 + " is " + rev_comp_if(seq1))
print("The reverse complementary strand of " +
      seq2 + " is " + rev_comp_if(seq2))
print("The reverse complementary strand of " +
      seq3 + " is " + rev_comp_if(seq3))
