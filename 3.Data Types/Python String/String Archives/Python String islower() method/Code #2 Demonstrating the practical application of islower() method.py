# Python3 code to demonstrate
# application of islower() method

# checking for proper nouns.
# nouns which start with capital letter

test_str = "Geeksforgeeks is most rated Computer Science portal and is highly recommended"

# splitting string
list_str = test_str.split()

count = 0

# counting lower cases
for i in list_str:
	if (i.islower()):
		count = count + 1

# printing proper nouns count
print ("Number of proper nouns in this sentence is : " + str(len(list_str)-count))
