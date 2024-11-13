# Python3 code to demonstrate
# Remove front K elements in String List
# using list comprehension + list slicing

# initializing list
test_list = ['Manjeet', 'Akash', 'Akshat', 'Nikhil']

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# using list comprehension + list slicing
# Remove front K elements in String List
res = [sub[K :] for sub in test_list]

# printing result
print("The list after removing initial K characters : " + str(res))
