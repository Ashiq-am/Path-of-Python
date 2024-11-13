# strings
str1 = "gfg"
str2 = "abc"
str3 = "gf"
original_string = "geeksforgeeks"
print("Initial string:", original_string)
translation = original_string.maketrans(str1, str2, str3)
# Altered String
print("Modified string:", original_string.translate(translation))
