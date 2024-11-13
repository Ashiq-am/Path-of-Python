# Python3 code to demonstrate working of
# Replace characters after K occurrences
# Using loop + string slices

# initializing string
test_str = "geeksforgeeks is best for geeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 2

# initializing Repl char
repl_char = "*"

# Replace characters after K occurrences
# Using loop + string slices
for sub in set(test_str):
	for idx in [idx for idx in range(len(test_str)) if test_str[idx] == sub][K:]:
		test_str = test_str[:idx] + repl_char + test_str[idx + 1:]

# printing result
print("The string after performing replace : " + test_str)
