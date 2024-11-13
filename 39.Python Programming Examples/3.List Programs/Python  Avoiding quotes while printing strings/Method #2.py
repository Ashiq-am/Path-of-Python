# Python3 code to demonstrate
# avoiding printing last comma
# using print() + sep

# initializing list
test_list = ['Geeks', 'For', 'Geeks']

# printing original list
print ("The original list is : " + str(test_list))

# using print() + sep
# avoiding printing last comma
print ("The formatted output is : ")
print(*test_list, sep =', ')
