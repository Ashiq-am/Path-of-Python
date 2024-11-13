import Levenshtein

ratio_seq = Levenshtein.seqratio("pqrst", "pqrtu")
print(f"The sequence ratio between 'pqrst' and 'pqrtu' is : {ratio_seq}")
