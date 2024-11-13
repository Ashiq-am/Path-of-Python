# Python code to demonstrate
# next() vs for loop
import time

# initializing list
list1 = [1, 2, 3, 4, 5]

# keeping list2
list2 = list1

# converting list to iterator
list1 = iter(list1)

print ("The contents of list are : ")

# printing using next()
# using default
start_next = time.time()
while (1) :
	val = next(list1,'end')
	if val == 'end':
		break
	else :
		print (val)
print ("Time taken for next() is : " + str(time.time() - start_next))

# printing using for loop
start_for = time.time()
for i in list2 :
	print (i)
print ("Time taken for loop is : " + str(time.time() - start_for))
