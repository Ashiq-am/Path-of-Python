import Levenshtein

jaro_dist = Levenshtein.jaro("bunty", "bunti")
print(f"The Jaro distance between 'bunty' and 'bunti' is : {jaro_dist}")
