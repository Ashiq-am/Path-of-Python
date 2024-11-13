# Python3 code to demonstrate working of
# Extract Nth words in Strings List
# Using list comprehension + split()

# initializing list
test_list = ['Gfg best for', 'All geeks', 'It is for', 'all CS professionals']

# printing original list
print("The original list is : " + str(test_list))

# initializing N
N = 2

# Extract Nth words in Strings List
# Using list comprehension + split()
res = [sub.split()[N - 1] for sub in test_list if len(sub.split()) > 1]

# printing result
print("The Nth words in list are : " + str(res))
