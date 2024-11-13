# Python program to remove common elements
# in the two lists using list comprehension
def remove_common(a, b):

	a, b = [i for i in a if i not in b],
	[j for j in b if j not in a]

	print("list1 : ", a)
	print("list2 : ", b)

if __name__ == "__main__":

	a = [1, 2, 3, 4, 5]
	b = [4, 5, 6, 7, 8]

	remove_common(a, b)
