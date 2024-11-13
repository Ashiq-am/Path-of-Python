# convert rdd to list by using map() method
b = rdd.map(list)

# display the data in b with collect method
for i in b.collect():
	print(i)
