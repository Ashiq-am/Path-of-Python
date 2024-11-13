# Python3 code to demonstrate working of
# Sort Dictionary by Values Summation
# Using map() + dictionary comprehension + sorted() + sum()

# initializing dictionary
test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3, 2], 'best' : [7, 6, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# summing all the values using sum()
# map() is used to extend summation to sorted()
temp = {key: sum(map(lambda ele: ele, test_dict[key])) for key in test_dict}
res = {key: temp[key] for key in sorted(temp, key = temp.get)}

# printing result
print("The sorted dictionary : " + str(res))
