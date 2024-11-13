# initialise the empty list of store the list of list
listOfList = list()

# create list which will be passed as parameter in the zip
list1 = [1, 4, 7]
list2 = [2, 5, 8]
# this list has one extra item which will be dropped
list3 = [3, 6, 9, 10]

# iterate on the corresponding element in each list
for element1, element2, element3 in zip(list1, list2, list3):
	# create a list by using corresponding element from each list
	rowList = list([element1, element2, element3])
	# append the rowList in the main list
	listOfList.append(rowList)

# Display the output
print(listOfList)
