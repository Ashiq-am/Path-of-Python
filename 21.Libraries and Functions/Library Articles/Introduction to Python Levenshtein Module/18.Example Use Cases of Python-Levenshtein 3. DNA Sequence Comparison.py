import Levenshtein

dna1 = "ACTGAG"
dna2 = "ACGGAG"

distance = Levenshtein.distance(dna1, dna2)
print(f"Levenshtein distance between DNA sequences: {distance}")
