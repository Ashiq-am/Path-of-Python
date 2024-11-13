# Python3 code to demonstrate working of
# Replace characters after K occurrences
# Using join() + count() + enumerate()

# initializing string
test_str = "geeksforgeeks is best for geeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 2

# initializing Repl char
repl_char = "*"

# Replace characters after K occurrences
# Using join() + count() + enumerate()
res = "".join(chr if test_str.count(chr, 0, idx) < K
	else repl_char for idx, chr in enumerate(test_str))

# printing result
print("The string after performing replace : " + res)
