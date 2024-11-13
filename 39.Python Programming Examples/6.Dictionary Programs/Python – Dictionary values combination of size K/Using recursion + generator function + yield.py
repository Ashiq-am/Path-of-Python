# Python3 code to demonstrate working of
# Dictionary values combination of size K
# Using yield + generator function + recursion

def gen_strs(chr_key, test_dict, K):
	def hlpr(s):
		if len(s) == K:
			yield s
		elif len(s) < K:
			for ltr in test_dict[s[-1]]:
				yield from hlpr(s + ltr)
	for ltr in chr_key:
		yield from hlpr(ltr)

# initializing dictionary
test_dict = {'a' : 'abc', 'b' : 'bd', 'c' : 'c', 'd' : 'ab'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing K
K = 3

# initializing character keys
chr_key = 'abcd'

# Dictionary values combination of size K
# Using yield + generator function + recursion
res = []
for ele in gen_strs(chr_key, test_dict, K):
	res.append(ele)

# printing result
print("The extracted combinations : " + str(res))
