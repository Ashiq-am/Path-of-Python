import Levenshtein

name1 = "Jonathon"
name2 = "Jonathan"

similarity = Levenshtein.ratio(name1, name2)
if similarity > 0.8:
    print(f"The names '{name1}' and '{name2}' are likely the same.")
