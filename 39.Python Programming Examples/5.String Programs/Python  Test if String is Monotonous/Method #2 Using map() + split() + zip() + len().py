# Python3 code to demonstrate working of
# Test if String is Monotonous
# Using map() + split() + zip() + len()

# initializing string
test_str = "6, 5, 4, 3, 2, 1"

# printing original string
print("The original string is : " + test_str)

# initializing delim
delim = ", "

# Test if String is Monotonous
# Using map() + split() + zip() + len()
temp = list(map(int, test_str.split(delim)))
diff = set(i - j for i, j in zip(temp, temp[1:]))
res = len(diff) == 1 and diff.pop() in (1, -1)

# printing result
print("Is string Monotonous ? : " + str(res))
