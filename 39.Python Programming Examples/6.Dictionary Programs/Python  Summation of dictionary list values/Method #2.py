# Python3 code to demonstrate working of
# Summation of dictionary list values
# using sum() + map()

# initialize dictionary
test_dict = {'gfg' : [5, 6, 7], 'is' : [10, 11], 'best' : [19, 31, 22]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Summation of dictionary list values
# using sum() + map()
res = sum(map(len, test_dict.values()))

# printing result
print("Summation of dictionary list values are : " + str(res))
