# initialise the empty list to store list of list
listOfList = []

for row in range(0, 3):
	# for each row generate a list which contain the 3 elements in it
	# generated using list comprehension
	rowList = [element for element in range(row, row+3)]
	# put the rowList in the list of list
	listOfList.append(rowList)

# displaying the store values in listOfLits
print(listOfList)
