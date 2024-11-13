import Levenshtein

jaro_winkler_dist = Levenshtein.jaro_winkler("Rudra", "Rudhra")
print(f"The Jaro Winkler distance between 'Rudra' and 'Rudhra' is : {jaro_winkler_dist}")
