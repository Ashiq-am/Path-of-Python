# Python3 code to demonstrate
# to extract words from string
# using split()

# initializing string
test_string = "GeeksforGeeks is a computer science portal for Geeks"

# printing original string
print("The original string is : " + test_string)

# using split()
# to extract words from string
res = test_string.split()

# printing result
print("\nThe words of string are")
for i in res:
    print(i)
