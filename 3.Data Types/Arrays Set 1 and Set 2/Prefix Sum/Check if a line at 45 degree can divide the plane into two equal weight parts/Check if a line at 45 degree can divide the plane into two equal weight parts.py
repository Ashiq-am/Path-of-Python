from collections import defaultdict

# Checking if a plane can be divide by a line
# at 45 degrees such that weight sum is equal
def is_partition_possible(n, x, y, w):
	weight_at_x = defaultdict(int)
	max_x = -2e3
	min_x = 2e3

	# Rotating each point by 45 degrees and
	# calculating prefix sum.
	# Also, finding maximum and minimum x
	# coordinates
	for i in range(n):
		new_x = x[i] - y[i]
		max_x = max(max_x, new_x)
		min_x = min(min_x, new_x)

		# storing weight sum upto x - y point
		weight_at_x[new_x] += w[i]
	sum_till = []
	sum_till.append(0)

	# Finding prefix sum
	for x in range(min_x, max_x + 1):
		sum_till.append(sum_till[-1] +
						weight_at_x[x])
	total_sum = sum_till[-1]
	partition_possible = False
	for i in range(1, len(sum_till)):
		if (sum_till[i] == total_sum - sum_till[i]):
			partition_possible = True

		# Line passes through i, so it neither
		# falls left nor right.
		if (sum_till[i - 1] == total_sum - sum_till[i]):
			partition_possible = True
	if partition_possible:
		print("YES")
	else:
		print("NO")

# Driven Program
if __name__ == "__main__":

	n = 3
	x = [-1, -2, 1]
	y = [1, 1, -1]
	w = [3, 1, 4]
	is_partition_possible(n, x, y, w)
