import Levenshtein

input = ["Ru", "Rud", "Rudra"]

median_str = Levenshtein.median(input)
print(f"The Median string in {input} is : {median_str}")
