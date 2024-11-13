# Python code to clone or copy a list
# Using bilt-in method copy()
def Cloning(li1):
	li_copy =[]
	li_copy = li1.copy()
	return li_copy

# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)
