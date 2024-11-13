# Python3 code to demonstrate working of
# Remove charcters greater than K
# Using join() + list comprehension + ord()

# initializing list
test_list = ["geeksforgeeks", "is", "best", "for", "geeks"]

# printing original lists
print("The original list is : " + str(test_list))

# initializing K
K = 13

# using list comprehension for 1 liner
res = [''.join([ele for ele in sub if ord(ele) - 97 <= K]) for sub in test_list]

# printing result
print("Filtered List " + str(res))
