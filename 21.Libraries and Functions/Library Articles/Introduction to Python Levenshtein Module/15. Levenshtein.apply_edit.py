import Levenshtein

edit_op = Levenshtein.editops("kitten", "sitting")
edit_applied = Levenshtein.apply_edit(edit_op, "kitten", "sitting")
print(f"The applied edit: {edit_applied}")
