# Python3 program to Check if a list is
# contained in another list without breaking order

def removeElements(A, B):
	for i in range(len(B)-len(A)+1):
		for j in range(len(A)):
			if B[i + j] != A[j]:
				break
		else:
			return True
	return False

# Driver code
A = [1, 2]
B = [1, 2, 3, 1, 1, 2, 2]
print(removeElements(A, B))
