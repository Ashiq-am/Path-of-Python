# Python3 code to demonstrate working of
# Convert tuple to adjacent pair dictionary
# using dict() + dictionary comprehension + slicing

# initialize tuple
test_tup = (1, 5, 7, 10, 13, 5)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Convert tuple to adjacent pair dictionary
# using dict() + dictionary comprehension + slicing
res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))

# printing result
print("Dictionary converted tuple : " + str(res))
