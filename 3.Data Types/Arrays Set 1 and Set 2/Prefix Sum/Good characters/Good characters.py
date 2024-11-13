MAX_CHARS = 26

def count_good_characters(A, K):
	n = len(A)
	ans = 0

	for o in range(MAX_CHARS):
		mp = [0] * (2 * n + 1) # Initialize frequency array
		mp[n] = 1 # Initialize with one occurrence to handle empty substring case

		occurrence = 0
		total = n
		prefix_sum = [n] * (n + 1)

		for i in range(n):
			x = 1 if A[i] == chr(ord('a') + o) else -1
			occurrence += x
			total += x
			prefix_sum[i + 1] = total
			ans += mp[total - K]

			# Check for substrings with negative length
			if K < 0 and (i + 1 + K >= 0) and (prefix_sum[i + 1 + K] == total - K):
				ans -= 1

			mp[total] += 1

	return ans

def main():
	N, K = 4, -1
	A = "abac"

	result = count_good_characters(A, K)

	# Output the result
	print(result)

if __name__ == "__main__":
	main()
