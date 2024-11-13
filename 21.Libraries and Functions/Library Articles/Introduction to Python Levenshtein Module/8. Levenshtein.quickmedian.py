import Levenshtein
input = ["Ru", "Rud", "Rudra"]

quick_median = Levenshtein.quickmedian(input)
print(f" The quick median in {input} is : {quick_median}")
