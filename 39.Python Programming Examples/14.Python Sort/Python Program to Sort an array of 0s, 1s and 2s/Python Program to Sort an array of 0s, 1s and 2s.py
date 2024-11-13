# Function for sort
import array


def SortWithoutSorting(arr):
# 3 Empty list for initialize 0 1 and 2

	l1 =[]
	l2 =[]
	l3 =[]
	for i in range(len(arr)):
		if arr[i] == 0:
			l1.append(arr[i])
		elif arr[i] == 1:
			l2.append(arr[i])
		else:
			l3.append(arr[i])
	return (l1 + l2 + l3)

# Driver Code
arr = array.array('i', [0, 1, 0, 1, 2, 2, 0, 1])
print(SortWithoutSorting(arr))
