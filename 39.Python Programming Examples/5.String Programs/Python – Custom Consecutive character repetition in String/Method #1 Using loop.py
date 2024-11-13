# Python3 code to demonstrate working of
# Custom Consecutive character repetition in String
# Using loop

# initializing string
test_str = 'Geeks4Geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing dictionary
test_dict = {"G": 3, "e": 2, "4": 4, "k": 5, "s": 3}

res = ""
for ele in test_str:
    # using * operator for repetition
    # using + for concatenation
    res += ele * test_dict[ele]

# printing result
print("The filtered string : " + str(res))
