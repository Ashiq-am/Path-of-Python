class Solution:
	def klengthpref(self, arr, n, k, s):
		a = s[:k] # storing k-length substring of str
		count = 0 # counter to count the matching condition

		# looping through each word of arr
		for i in range(n):
			if(len(arr[i]) < k): # if the length of string from arr is less than k
				continue # then there is no point in finding the substring so we skip
			t = arr[i]
			b = t[:k] # storing k-length substring of each string from arr
			if(a == b): # checking equality of the two substring a and b
				count += 1 # if condition matches increase the counter by 1
		return count # finally return the count


arr = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
str = "abbg"
n = len(arr)
k = 3

obj = Solution()
print(obj.klengthpref(arr, n, k, str))
