# Python program to remove common elements
# in the two lists using remove method
def remove_common(a, b):

	for i in a[:]:
		if i in b:
			a.remove(i)
			b.remove(i)

	print("list1 : ", a)
	print("list2 : ", b)

if __name__ == "__main__":

	a = [1, 2, 3, 4, 5]
	b = [4, 5, 6, 7, 8]

	remove_common(a, b)
