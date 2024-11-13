import Levenshtein

check_sim = Levenshtein.ratio("orange", "oranges")
print(f"The similarity ratio between 'orange' and 'oranges' is : {check_sim}")
