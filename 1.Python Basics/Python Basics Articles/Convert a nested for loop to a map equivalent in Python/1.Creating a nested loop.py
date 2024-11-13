# create two sample lists lst1 and lst2 as shown
lst1 = [10, 20, 30]
lst2 = [3, 4, 5]

# this empty list stores the output
result = []

# Now, run a nested for loop
# add every element of the lst1 to all elements of lst2
# store the output in a separate list
for i in lst1:
	for j in lst2:
		result.append(i+j)

# print the result
print(result)
