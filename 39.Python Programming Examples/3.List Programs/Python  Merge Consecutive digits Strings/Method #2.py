# Python3 code to demonstrate
# Merge Consecutive digits Strings
# using regex() + join()
import re

# Initializing list
test_list = ['g', '1', '2', 'i', '5', 'b', '6', '7']

# printing original list
print("The original list is : " + str(test_list))

# Merge Consecutive digits Strings
# using regex() + join()
res = re.findall('\d+|.', ''.join(test_list))

# printing result
print ("List after digit merge : " + str(res))
