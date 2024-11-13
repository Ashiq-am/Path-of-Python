# Python3 code to demonstrate
# to check if list is subset of other

# initializing list
one = [1,2,3,4,5]
two = [1,2]

#using set to find if element exsists in another list
result = set(x in one for x in two)

flag = 0

for ans in result:
	if ans == False:
		flag=1

#Printing list
print ("Original list : " + str(one))
print ("Original sub list : " + str(two))

if flag==0:
	print("Yes, list is subset of other.")
else:
	print("No, list is not subset of other.")

