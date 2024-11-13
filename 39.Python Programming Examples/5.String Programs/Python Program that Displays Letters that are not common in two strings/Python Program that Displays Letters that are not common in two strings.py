# taking string inputs
string_1 = "hi"
string_2 = "ASHIQ"

# letters which are present in the two strings
# but not in both are found using the ‘^’ operator
e = list(set(string_1) ^ set(string_2))

# printing finale list
print("The letters are:")
for i in e:
	print(i)
