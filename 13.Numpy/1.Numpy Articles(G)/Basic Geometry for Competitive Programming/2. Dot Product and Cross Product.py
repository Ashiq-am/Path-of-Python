class VectorOperations:
	@staticmethod
	def dot_product(vec1, vec2):
		result = 0
		for i in range(3):
			result += vec1[i] * vec2[i]
		return result

	@staticmethod
	def cross_product(vec1, vec2):
		result = [0.0, 0.0, 0.0]
		result[0] = vec1[1] * vec2[2] - vec1[2] * vec2[1]
		result[1] = vec1[2] * vec2[0] - vec1[0] * vec2[2]
		result[2] = vec1[0] * vec2[1] - vec1[1] * vec2[0]
		return result

if __name__ == "__main__":
	# Example vectors
	vector1 = [1.0, 2.0, 3.0]
	vector2 = [4.0, 5.0, 6.0]

	# Calculate and display the dot product
	dot_result = VectorOperations.dot_product(vector1, vector2)
	print("Dot Product:", dot_result)

	# Calculate and display the cross product
	cross_result = VectorOperations.cross_product(vector1, vector2)
	print("Cross Product:", cross_result)
