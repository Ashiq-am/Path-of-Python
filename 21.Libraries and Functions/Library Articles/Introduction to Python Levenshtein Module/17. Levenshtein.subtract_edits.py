from Levenshtein import editops, apply_edit, subtract_edit

a = "man"
b = "woman"

e = editops(a, b)
print('e:', e)
e1 = e[:2]
print('e1:', e1)

app_edit = apply_edit(e1, 'man', 'woman')
print('app_edit:', app_edit)

sub_edit = apply_edit(subtract_edit(e, e1), app_edit, 'scotsman')
print('edit:', sub_edit)
