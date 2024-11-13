# Python3 code to demonstrate working of
# Common list elements and dictionary values
# Using set() and intersection()

# initializing list
test_list = ["Gfg", "is", "Best", "For", "Geeks"]

# printing original list
print("The original list : " + str(test_list))

# initializing subs. Dictionary
subs_dict = {4: "Gfg", 8: "Geeks", 9: " Good", }

# Intersection of elements, using set() to convert
# intersection() for common elements
res = list(set(test_list).intersection(list(subs_dict.values())))

# printing result
print("Intersection elements : " + str(res))
