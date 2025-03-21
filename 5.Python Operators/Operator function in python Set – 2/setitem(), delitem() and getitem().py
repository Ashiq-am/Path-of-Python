# Python code to demonstrate working of
# setitem(), delitem() and getitem()

# importing operator module
import operator

# Initializing list
li = [1, 5, 6, 7, 8]

# printing original list
print ("The original list is : ",end="")
for i in range(0,len(li)):
	print (li[i],end=" ")

print ("\r")

# using setitem() to assign 3 at 4th position
operator.setitem(li,3,3)

# printing modified list after setitem()
print ("The modified list after setitem() is : ",end="")
for i in range(0,len(li)):
	print (li[i],end=" ")

print ("\r")

# using delitem() to delete value at 2nd index
operator.delitem(li,1)

# printing modified list after delitem()
print ("The modified list after delitem() is : ",end="")
for i in range(0,len(li)):
	print (li[i],end=" ")

print ("\r")

# using getitem() to access 4th element
print ("The 4th element of list is : ",end="")
print (operator.getitem(li,3))
