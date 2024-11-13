# Python code for the above approach:

def prefixSuffixString(s1, s2):
	count = 0
	for s in s2:
		for t in s1:
			if t.startswith(s) or t.endswith(s):
				count += 1
				break
	return count

if __name__ == "__main__":
	s1 = ["cat", "catanddog", "lion"]
	s2 = ["cat", "dog", "rat"]

	print(prefixSuffixString(s1, s2))
