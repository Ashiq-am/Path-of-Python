import Levenshtein
input = ["Ru", "Rud", "Rudra"]

improved_median = Levenshtein.median_improve("Ru", input)
print(f"Improved median in {input} is : {improved_median}")
