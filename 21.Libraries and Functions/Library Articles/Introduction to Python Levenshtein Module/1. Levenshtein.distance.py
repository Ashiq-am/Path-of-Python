import Levenshtein

input1 = "cooking"
input2 = "looking"

dist_calc = Levenshtein.distance(input1, input2)

print(f"The Levenshtein distance between {input1} and {input2} is : {dist_calc}")
