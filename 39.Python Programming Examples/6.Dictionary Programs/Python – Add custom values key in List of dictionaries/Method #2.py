# Python3 code to demonstrate working of
# Add custom values key in List of dictionaries
# Using zip() + loop

# initializing lists
test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},
			{"Gfg" : 8, "is" : 11, "best" : 19},
			{"Gfg" : 2, "is" : 16, "best" : 10},
			{"Gfg" : 12, "is" : 1, "best" : 8},
			{"Gfg" : 22, "is" : 6, "best" : 8}]

# printing original list
print("The original list : " + str(test_list))

# initializing Key
K = "CS"

# initializing list
append_list = [6, 7, 4, 3, 9]

# zip() used to bind index wise
# list and dictionary
for dic, lis in zip(test_list, append_list):
    dic[K] = lis

# printing result
print("The dictionary list after addition : " + str(test_list))
