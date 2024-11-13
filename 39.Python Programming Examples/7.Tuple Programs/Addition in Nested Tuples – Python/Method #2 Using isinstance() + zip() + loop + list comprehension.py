# Python3 code to demonstrate working of
# Addition in nested tuples
# using isinstance() + zip() + loop + list comprehension

# function to perform task
def tup_sum(tup1, tup2):
    if isinstance(tup1, (list, tuple)) and isinstance(tup2, (list, tuple)):
        return tuple(tup_sum(x, y) for x, y in zip(tup1, tup2))

    return tup1 + tup2

# initialize tuples
test_tup1 = ((1, 3), (4, 5), (2, 9), (1, 10))
test_tup2 = ((6, 7), (3, 9), (1, 1), (7, 3))

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Addition in nested tuples
# using isinstance() + zip() + loop + list comprehension
res = tuple(tup_sum(x, y) for x, y in zip(test_tup1, test_tup2))

# printing result
print("The resultant tuple after summation : " + str(res))
