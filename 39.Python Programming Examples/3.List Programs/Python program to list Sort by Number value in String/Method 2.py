# initializing Matrix
test_list = ["all no 100", "gfg is", "geeks over seas 62", "and planets 3"]

# printing original list
print("The original list is : " + str(test_list))

# performing sorting
# lambda function injecting functionality
res = sorted(test_list, key=lambda strn: -1
			if len([ele for ele in strn.split()
					if ele.isdigit()]) == 0
			else int([ele for ele in strn.split()
					if ele.isdigit()][0]))

# printing result
print("Sorted Strings : " + str(res))
