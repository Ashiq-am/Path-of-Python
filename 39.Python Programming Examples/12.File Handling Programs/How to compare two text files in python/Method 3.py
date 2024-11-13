import filecmp

d1 = "C:/Users/user/Documents/"
d2 = "C:/Users/user/Desktop/"
files = ['intro.txt']

# shallow comparison
match, mismatch, errors = filecmp.cmpfiles(d1, d2, files)
print('Shallow comparison')
print("Match:", match)
print("Mismatch:", mismatch)
print("Errors:", errors)

# deep comparison
match, mismatch, errors = filecmp.cmpfiles(d1, d2, files, shallow=False)
print('Deep comparison')
print("Match:", match)
print("Mismatch:", mismatch)
print("Errors:", errors)
