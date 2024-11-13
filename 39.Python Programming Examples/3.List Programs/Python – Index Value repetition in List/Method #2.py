# Python3 code to demonstrate working of
# Index Value repetition in List
# Using chain.from_iterable() + list comprehension
import itertools

# initializing Matrix
test_list = [3, 0, 4, 2]

# printing original list
print("The original list is : " + str(test_list))

# enumerate() gets index and
# value of similar index element
# from_iterable() used to flatten
res = list(itertools.chain(*([idx] * ele for idx,
                                             ele in enumerate(test_list))))

# printing result
print("Constructed List : " + str(res))
