# python code to demonstrate
# splitting nested list
# into 2 lists

# initialising nested lists
ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]]

# printing initial lists
print ("initial list", str(ini_list))

# code to split it into 2 lists
res1 = [i[1] for i in ini_list]
res2 = [i[0] for i in ini_list]

# printing result
print("final lists", str(res1), "\n", str(res2))
