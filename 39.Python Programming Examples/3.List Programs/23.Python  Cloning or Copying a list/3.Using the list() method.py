# Python code to clone or copy a list
# Using the in-built function list()
def Cloning(li1):
	li_copy = list(li1)
	return li_copy

# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
