# Python3 code to demonstrate working of
# Nth Column vertical string in Matrix
# Using join() + list comprehension

# initializing list
test_list = [('a', 'g', 'v'), ('e', 'f', 8), ('b', 'g', 0)]

# printing list
print("The original list : " + str(test_list))

# initializing Nth column
N = 1

# Nth Column vertical string in Matrix
# Using join() + list comprehension
temp = [sub[N] for sub in test_list]
res = "".join(temp)

# Printing result
print("Constructed vertical string : " + str(res))
