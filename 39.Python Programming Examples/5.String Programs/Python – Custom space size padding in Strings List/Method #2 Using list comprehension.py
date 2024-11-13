# Python3 code to demonstrate working of
# Custom space size padding in Strings List
# Using list comprehension

# initializing lists
test_list = ["Gfg", "is", "Best"]

# printing original list
print("The original list is : " + str(test_list))

# initializing padding numbers
lead_size = 3
trail_size = 2

# using list comprehension for one liner alternative
res = [(lead_size * ' ') + ele + (trail_size * ' ') for ele in test_list]

# printing result
print("Padded Strings : " + str(res))
