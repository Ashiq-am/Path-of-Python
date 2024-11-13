import Levenshtein

edit_op = Levenshtein.editops("kitten", "sitting")
inv_op = Levenshtein.inverse(edit_op)
print(f"The inverse of {edit_op} is : {inv_op}")
