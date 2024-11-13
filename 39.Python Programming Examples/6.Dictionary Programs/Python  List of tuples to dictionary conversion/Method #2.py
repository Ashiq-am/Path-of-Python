# Python3 code to demonstrate
# List of tuple to dictionary conversion
# using dict() + dictionary comprehension

# initializing list
test_list = [('Nikhil', 21, 'JIIT'), ('Akash', 22, 'JIIT'), ('Akshat', 22, 'JIIT')]

# printing original list
print("The original list : " + str(test_list))

# using dict() + dictionary comprehension
# List of tuple to dictionary conversion
res = dict((idx[0], idx[1:]) for idx in test_list)

# print result
print("The dictionary after conversion : " + str(res))
