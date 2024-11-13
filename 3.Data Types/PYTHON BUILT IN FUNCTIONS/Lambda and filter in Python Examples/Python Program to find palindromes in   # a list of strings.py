# Python Program to find palindromes in
# a list of strings.

my_list = ["geeks", "geeg", "keek", "practice", "aa"]

# use anonymous function to filter palindromes.
# Please refer below article for details of reversed
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))

# printing the result
print(result)
