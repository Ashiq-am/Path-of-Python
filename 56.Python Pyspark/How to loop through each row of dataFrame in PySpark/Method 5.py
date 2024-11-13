# using list comprehension for looping
# through each row storing the list of
# data in the variable
table = [x["Job Profile"] for x in df.rdd.collect()]

# looping the list for printing
for row in table:
	print(row)
