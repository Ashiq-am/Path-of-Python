# Python3 code to demonstrate working of
# Fill Strings for size K in Tuple List
# Using list comprehension + ljust()

# initializing list
test_list = [('Gfg', 'is'), ('best', 'for'), ('CS', 'Geeks')]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 8

# initializing fill_char
fill_char = '*'

# Fill Strings for size K in Tuple List
# Using list comprehension + ljust()
res = [(a.ljust(K, fill_char), b.ljust(K, fill_char)) for a, b in test_list]

# printing result
print("The modified list : " + str(res))
