# Python3 code to demonstrate
# to initialize multiple lists
# using loop

# using loop
# to initialize multiple lists
list1, list2, list3, list4 = ([] for i in range(4))

# printing lists
print ("The initialized lists are : ")
print ("List 1 : " + str(list1))
print ("List 2 : " + str(list2))
print ("List 3 : " + str(list3))
print ("List 4 : " + str(list4))
