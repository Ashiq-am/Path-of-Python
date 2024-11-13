# Python3 code to demonstrate working of
# Nth column Maximum in tuple list
# using list comprehension + max()

# initialize list
test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

# printing original list
print("The original list is : " + str(test_list))

# initialize N
N = 2

# Nth column Maximum in tuple list
# using list comprehension + max()
res = max([sub[N] for sub in test_list])

# printing result
print("Maximum of Nth Column of Tuple List : " + str(res))
