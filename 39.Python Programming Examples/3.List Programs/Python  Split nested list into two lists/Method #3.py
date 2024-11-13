# python code to demonstrate
# splitting nested list
# into 2 lists

from operator import itemgetter

# initialising nested lists
ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]]

# printing initial lists
print ("initial list", str(ini_list))

# code to split it into 2 lists
res1 = list(map(itemgetter(0), ini_list))
res2 = list(map(itemgetter(1), ini_list))

# printing result
print("final lists", str(res1), "\n", str(res2))
