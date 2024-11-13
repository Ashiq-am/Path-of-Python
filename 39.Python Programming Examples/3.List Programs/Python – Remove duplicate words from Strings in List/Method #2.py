# Python3 code to demonstrate
# Remove duplicate words from Strings in List
# using list comprehension + set() + split()

# Initializing list
test_list = ['gfg, best, gfg', 'I, am, I', 'two, two, three']

# printing original list
print("The original list is : " + str(test_list))

# Remove duplicate words from Strings in List
# using list comprehension + set() + split()
res = [set(strs.split(", ")) for strs in test_list]

# printing result
print("The list after duplicate words removal is : " + str(res))
