# Python3 code to demonstrate
# finding frequency in list of tuples
# using Counter() + list comprehension
from collections import Counter

# initializing list of tuples
test_list = [('Geeks', 1), ('for', 2), ('Geeks', 3)]

# printing the original list
print ("The original list is : " + str(test_list))

# using Counter() + list comprehension
# finding frequency in list of tuples
res = Counter(i[0] for i in test_list)

# printing result
print ("The frequency of element is : " + str(res['Geeks']))
