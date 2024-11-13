# list of tuple for student data
# with both integer and strings
a = [(1, 2,3,4,5),
	("sravan","bobby","ojaswi","rohith","Gnanesh"),
	(96,89,78,90,78)]

# display
print("Original list of tuple")
print(a)

# list of tuple for student data
# with both integer and strings
a = [(1, 2,3,4,5),
	("sravan","bobby","ojaswi","rohith","Gnanesh"),
	(96,89,78,90,78)]

# convert list of tuple to multiple lists
data = map(list, zip(*a))

print("")

# display
print("List")
for i in data:
	print(i)
