# Taking list1 input from user as list
list1 = list(input("Please Enter Elements of list1: "))

# Taking list2 input from user as list
list2 = list(input("Please Enter Elements of list2: "))


# appending list2 into list1 using .append function
for i in list2:
	list1.append(i)

# printing list1
print(list1)
