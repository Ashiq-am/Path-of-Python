# Python code to demonstrate
# to calculate difference
# between adjacent elements in list


# initialising _list
ini_list = [5, 4, 89, 12, 32, 45]

# printing iniial_list
print("intial_list", str(ini_list))

# Calculating difference list
diff_list = []

for i in range(1, len(ini_list)):
	diff_list.append(ini_list[i] - ini_list[i-1])

# printing difference list
print ("difference list: ", str(diff_list))
