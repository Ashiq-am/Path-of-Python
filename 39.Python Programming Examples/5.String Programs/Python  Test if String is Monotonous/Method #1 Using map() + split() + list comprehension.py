# Python3 code to demonstrate working of
# Test if String is Monotonous
# Using list comprehension + map() + split()

# initializing string
test_str = "6, 5, 4, 3, 2, 1"

# printing original string
print("The original string is : " + test_str)

# initializing delim
delim = ", "

# Test if String is Monotonous
# Using list comprehension + map() + split()
temp = list(map(int, test_str.split(delim)))
direc = temp[-1] > temp[0] or -1
res = temp == list(range(temp[0], temp[-1] + direc, direc))

# printing result
print("Is string Monotonous ? : " + str(res))
