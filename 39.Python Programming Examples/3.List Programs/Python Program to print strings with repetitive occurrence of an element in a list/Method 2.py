# initializing Matrix
test_list = ["geeksforgeeks", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 'e'

# checking for count greater than 1 (repetitive)
# one-liner using list comprehension
res = [ele for ele in test_list if ele.count(K) > 1]

# printing result
print("Repeated K strings : " + str(res))
