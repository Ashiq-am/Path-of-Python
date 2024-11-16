def add_vectors(v1, v2):
	result = []
	if len(v1) != len(v2):
		print("Vectors must be of the same size for addition.")
		return result # Returning an empty list indicating an error

	result = [x + y for x, y in zip(v1, v2)]
	return result

def subtract_vectors(v1, v2):
	result = []
	if len(v1) != len(v2):
		print("Vectors must be of the same size for subtraction.")
		return result # Returning an empty list indicating an error

	result = [x - y for x, y in zip(v1, v2)]
	return result

# Example vectors
vector1 = [1, 2, 3, 4, 5]
vector2 = [5, 4, 3, 2, 1]

# Perform vector addition
sum_result = add_vectors(vector1, vector2)
print("Vector Addition Result:", *sum_result)

# Perform vector subtraction
difference_result = subtract_vectors(vector1, vector2)
print("Vector Subtraction Result:", *difference_result)
