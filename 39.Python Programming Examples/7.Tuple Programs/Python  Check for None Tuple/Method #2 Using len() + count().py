# Python3 code to demonstrate working of
# Check for None Tuple
# using len() + count()

# initialize tuple
test_tup = (None, None, None, None, None)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Check for None Tuple
# using len() + count()
res = len(test_tup) == test_tup.count(None)

# printing result
print("Does tuple contain all None elements ? : " + str(res))
