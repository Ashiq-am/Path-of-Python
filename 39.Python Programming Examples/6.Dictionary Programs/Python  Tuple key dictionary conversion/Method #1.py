# Python3 code to demonstrate
# Tuple key dictionary conversion
# using list comprehension

# initializing list
test_list = [('Nikhil', 21, 'JIIT'), ('Akash', 22, 'JIIT'), ('Akshat', 22, 'JIIT')]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# Tuple key dictionary conversion
res = {(sub[0], sub[1]): sub[2:] for sub in test_list}

# print result
print("The dictionary after conversion : " + str(res))
