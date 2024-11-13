# Python3 code to demonstrate working of
# Check for None Tuple
# using all() + generator expression

# initialize tuple
test_tup = (None, None, None, None, None)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Check for None Tuple
# using all() + generator expression
res = all(ele is None for ele in test_tup)

# printing result
print("Does tuple contain all None elements ? : " + str(res))
