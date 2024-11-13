class GFG:

	@staticmethod

	def check_triplets(A):

		# Variable to store length of A

		n = len(A)

		# Variable to store count of valid triplets

		count = 0

		# Loops for making combination all possible triplets

		for i in range(n - 2):

			for j in range(i + 1, n - 1):

				for k in range(j + 1, n):

					# Check if the triplet has at most 2 identical elements

					if A[i] != A[j] or A[j] != A[k]:

						count += 1

		return count

	# Main Function

	def main():

		# Input A[]

		A = [5, 5, 2, 5]

		# Function call

		print(GFG.check_triplets(A))

# Running the main function

GFG.main()
