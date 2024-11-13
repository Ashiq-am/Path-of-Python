# Python program to demonstrate
# working of keys()

# initializing dictionary
test_dict = { "geeks" : 7, "for" : 1, "geeks" : 2 }

# accessing 2nd element using naive method
# using loop
j = 0
for i in test_dict:
	if (j == 1):
		print ('2nd key using loop : ' + i)
	j = j + 1

# accessing 2nd element using keys()
print ('2nd key using keys() : ' + test_dict.keys()[1])
