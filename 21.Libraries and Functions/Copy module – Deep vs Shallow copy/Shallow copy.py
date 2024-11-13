""""""




'''A shallow copy means constructing a new collection object and then populating it with references to the 
child objects found in the original. 

The copying process does not recurse and therefore won’t create copies of the child objects themselves. 
In case of shallow copy, a reference of object is copied in other object. 
It means that any changes made to a copy of object do reflect in the original object. 

In python, this is implemented using “copy()” function.'''





# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# original elements of list
print ("The original elements before shallow copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# checking if change is reflected
print ("The original elements after shallow copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")





"""In the above example, the change made in the list did effect in other list, indicating the list is shallow copied."""


