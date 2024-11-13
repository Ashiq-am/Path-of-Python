# Python3 code to demonstrate working of
# True Record
# using any() + map() + lambda + not

# initialize tuple
test_tup = (True, True, True, True)

# printing original tuple
print("The original tuple : " + str(test_tup))

# True Record
# using any() + map() + lambda + not
res = not any(map(lambda ele: not ele, test_tup))

# printing result
print("Is Tuple True ? : " + str(res))
