# Python program to sort the list
# alphabetically in a dictionary

dict ={
	"L1":["Geeks", "for", "Geeks"],
	"L2":["A", "computer", "science"],
	"L3":["portal", "for", "geeks"],
}

print("\nBefore Sorting: ")
for x in dict.items():
	print(x)

print("\nAfter Sorting: ")
for i, j in dict.items():
	sorted_dict ={i:sorted(j)}
	print(sorted_dict)
