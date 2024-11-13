# Python3 code to demonstrate working of
# Character coordinates in Matrix
# Using enumerate() + list comprehension + isalpha()

# initializing list
test_list = ['23f45.;4d', '5678d56d', '789', '5678g']

# printing original list
print("The original list is : " + str(test_list))

# Character coordinates in Matrix
# Using enumerate() + list comprehension + isalpha()
res = [(x, y) for x, val in enumerate(test_list)
       for y, chr in enumerate(val) if chr.isalpha()]

# printing result
print("Character indices : " + str(res))
