import Levenshtein

input = ["Ru", "Rud", "Rudra"]

set_med = Levenshtein.setmedian(input)
print(f" The set median in {input} is : {set_med}")
