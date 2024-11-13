#Python code for the above approach
from typing import List

# Function performing calculation
def MaxXor(N: int, Arr: List[int], Queries: List[int], K: int) -> List[int]:
	answer = []
	preXor = 0

	# Precomputing the Xor of the array
	for i in range(N):
		preXor = (preXor ^ Arr[i])

	# Right hand side variable which have
	# to be maximum
	rhs = (1 << K) - 1

	for i in range(N):
		# Updating preXor for each update
		# query and the result in
		# answer array
		preXor = (preXor ^ Arr[i])
		preXor = (preXor ^ Queries[i])
		answer.append(rhs ^ preXor)

	# Returning the answer array
	return answer

# Function for printing the array
def print_ans(N: int, answer: List[int]):
	for i in range(N):
		print(answer[i], end = " ")
	print()

# Driver code
if __name__ == "__main__":
	N = 4
	Arr = [2, 3, 4, 7]
	Queries = [1, 0, 3, 4]
	K = 4

	# Function call
	answer = MaxXor(N, Arr, Queries, K)

	# Function call to print
	print_ans(N, answer)

	# This code is contributed by lokehpotta20.
