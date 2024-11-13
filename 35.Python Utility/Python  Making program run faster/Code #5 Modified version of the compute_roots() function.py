import math

def compute_roots(nums):
	sqrt = math.sqrt
	result = []
	result_append = result.append
	for n in nums:
		result_append(sqrt(n))
	return result
