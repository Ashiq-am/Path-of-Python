# Python3 code to demonstrate working of
# List elements and dictionary values intersection
# Using list comprehension + values()

# initializing list
test_list = ["Gfg", "is", "Best", "For", "Geeks"]

# printing original list
print("The original list : " + str(test_list))

# initializing subs. Dictionary
subs_dict = {4: "Gfg", 8: "Geeks", 9: " Good", }

# Intersection of elements, using "in" for checking presence
res = [ele for ele in test_list if ele in subs_dict.values()]

# printing result
print("Intersection elements : " + str(res))
