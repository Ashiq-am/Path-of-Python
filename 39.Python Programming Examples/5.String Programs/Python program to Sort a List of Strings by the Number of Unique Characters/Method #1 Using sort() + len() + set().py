# Python3 code to demonstrate working of
# Sort Strings by Unique characters
# Using sort() + len() + set()

# helper function
def hlper_fnc(ele):
    # getting Unique elements count
    return len(list(set(ele)))


# initializing list
test_list = ['gfg', 'best', 'for', 'geeks']

# printing original list
print("The original list is : " + str(test_list))

# perform sort
test_list.sort(key=hlper_fnc)

# printing result
print("Sorted List : " + str(test_list))
