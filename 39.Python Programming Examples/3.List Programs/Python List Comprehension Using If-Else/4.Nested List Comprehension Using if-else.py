string = "G1"
firstList = ["Harsha", "Krishna", "Gowtham", "Vasanth Kumar", "Raghav"]

list_comp = [[k for k in firstList] if i.isalpha(
) else [j for j in range(1, 6)] for i in string]

print("Using the nested comprehension in the Python along with the if /else ")
for i in list_comp:
	print(i)
