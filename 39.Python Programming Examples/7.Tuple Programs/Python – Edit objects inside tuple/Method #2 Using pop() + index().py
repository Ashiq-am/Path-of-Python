# Python3 code to demonstrate working of
# Edit objects inside tuple
# Using pop() + index()

# initializing tuple
test_tuple = (1, [5, 6, 4], 9, 10)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Edit objects inside tuple
# Using pop() + index()
test_tuple[1].pop(2)
test_tuple[1].insert(2, 14)

# printing result
print("The modified tuple : " + str(test_tuple))
