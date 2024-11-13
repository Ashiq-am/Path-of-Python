# Python3 code to demonstrate working of
# Check if tuple has any None value
# using not + all()

# initialize tuple
test_tup = (10, 4, 5, 6, None)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Check if tuple has any None value
# using not + all()
res = not all(test_tup)

# printing result
print("Does tuple contain any None value ? : " + str(res))
