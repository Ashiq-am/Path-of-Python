import Levenshtein

word = "speling"
dictionary = ["spelling", "speaking", "spell", "splitting"]

closest_match = min(dictionary, key=lambda x: Levenshtein.distance(word, x))
print(f"Closest match for '{word}': {closest_match}")
