# Python3 code to demonstrate
# group similar substrings
# using lambda + itertools.groupby() + split()
from itertools import groupby

# initializing list
test_list = ['geek_1', 'coder_2', 'geek_4', 'coder_3', 'pro_3']

# sort list
# essential for grouping
test_list.sort()

# printing the original list
print ("The original list is : " + str(test_list))

# using lambda + itertools.groupby() + split()
# group similar substrings
res = [list(i) for j, i in groupby(test_list,
				lambda a: a.split('_')[0])]

# printing result
print ("The grouped list is : " + str(res))
