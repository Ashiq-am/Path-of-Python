# Python3 code to demonstrate working of
# Average String lengths in list
# using list comprehension + sum() + len()

# initialize list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Average String lengths in list
# using list comprehension + sum() + len()
temp = [len(ele) for ele in test_list]
res = 0 if len(temp) == 0 else (float(sum(temp)) / len(temp))

# printing result
print("The Average length of String in list is : " + str(res))
