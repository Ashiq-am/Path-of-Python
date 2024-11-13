# Python3 code to demonstrate working of
# Replace Different characters in String at Once
# using regex + lambda
import re

# initializing string
test_str = 'geeksforgeeks is best'

# printing original String
print("The original string is : " + str(test_str))

# initializing mapping dictionary
map_dict = {'e':'1', 'b':'6', 'i':'4'}

# using lambda and regex functions to achieve task
res = re.compile("|".join(map_dict.keys())).sub(lambda ele: map_dict[re.escape(ele.group(0))], test_str)

# printing result
print("The converted string : " + str(res))
