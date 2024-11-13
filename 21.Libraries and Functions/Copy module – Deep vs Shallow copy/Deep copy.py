""""""





'''Deep copy is a process in which the copying process occurs recursively. 
It means first constructing a new collection object and then recursively populating it with copies 
of the child objects found in the original. In case of deep copy, a copy of object is copied in other object. 

It means that any changes made to a copy of object do not reflect in the original object. 
In python, this is implemented using “deepcopy()” function.'''





# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]

# using deepcopy to deep copy
li2 = copy.deepcopy(li1)

# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(li1)):
	print (li1[i],end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# Change is reflected in l2
print ("The new list of elements after deep copying ")
for i in range(0,len( li1)):
	print (li2[i],end=" ")

print("\r")

# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")







'''In the above example, 
the change made in the list did not effect in other lists, indicating the list is deep copied.'''