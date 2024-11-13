# initialise an empty list which will store the list of list
listOfList = []

# this will create the number of rows
for row in range(0, 3):
	# for each row create an empty list to store the elements of that row
	rowList = []
	for column in range(row+1):
		rowList.append(column)
	# once we have complete the row list
	# we can put it into the original list of list
	listOfList.append(rowList)

# displaying the store values in
for eachList in listOfList:
	print(eachList)
