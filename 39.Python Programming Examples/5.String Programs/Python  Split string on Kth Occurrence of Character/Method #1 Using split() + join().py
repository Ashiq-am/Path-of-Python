# Python3 code to demonstrate working of
# Split string on Kth Occurrence of Character
# Using split() + join()

# initializing string
test_str = "Geeks_for_Geeks_is_best"

# split char
splt_char = "_"

# initializing K
K = 3

# printing original string
print("The original string is : " + str(test_str))

# Using split() + join()
# Split string on Kth Occurrence of Character
temp = test_str.split(splt_char)
res = splt_char.join(temp[:K]), splt_char.join(temp[K:])

# printing result
print("Is list after Kth split is : " + str(list(res)))
