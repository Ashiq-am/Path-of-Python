# initializing list
test_list = ["google", "is", "good", "goggled", "god"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 'g'

# appending and joining using list comprehension and join()
res = [''.join([ele for ele in sub if ele == K]) for sub in test_list]

# printing result
print("Modified List : " + str(res))
