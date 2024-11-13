''''''



"""Else block is executed in below Python 3.x program:"""


for i in range(1, 4):
	print(i)
else: # Executed because no break in for
	print("No Break")









"""Else block is NOT executed in below Python 3.x program:"""


for i in range(1, 4):
	print(i)
	break
else: # Not executed as there is a break
	print("No Break")




'''Such type of else is useful only if there is an if condition present inside the loop 
which somehow depends on the loop variable.

In the following example, the else statement will only be executed if no element of the 
array is even, 
i.e. if statement has not been executed for any iteration. 
Therefore for the array [1, 9, 8] the if is executed in third iteration of the loop and 
hence the else present after the for loop is ignored. In case of array [1, 3, 5] the if 
is not executed for any iteration and hence the else after the loop is executed.'''






# Python 3.x program to check if an array consists
# of even number
def contains_even_number(l):
	for ele in l:
		if ele % 2 == 0:
			print ("list contains an even number")
			break

	# This else executes only if break is NEVER
	# reached and loop terminated after all iterations.
	else:
		print ("list does not contain an even number")

# Driver code
print ("For List 1:")
contains_even_number([1, 9, 8])
print (" \nFor List 2:")
contains_even_number([1, 3, 5])










'''As an exercise, predict the output of following program'''


count = 0
while (count < 1):
	count = count+1
	print(count)
	break
else:
	print("No Break")
