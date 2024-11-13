# Python3 code to demonstrate working of
# Value summation of key in dictionary
# Using sum() + itemgetter() + map()
import operator

# Initialize list
test_list = [{'gfg' : 1, 'is' : 2, 'best' : 3},
			{'gfg' : 7, 'is' : 3, 'best' : 5},
			{'gfg' : 9, 'is' : 8, 'best' : 6}]

# printing original list
print("The original list is : " + str(test_list))

# Value summation of key in dictionary
# Using sum() + itemgetter() + map()
res = sum(map(operator.itemgetter('gfg'), test_list))

# printing result
print("The sum of particular key is : " + str(res))
