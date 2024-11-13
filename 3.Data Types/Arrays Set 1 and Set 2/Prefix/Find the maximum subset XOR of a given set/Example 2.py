class Solution:

	@staticmethod
	def findMaximumXOR(nums):

		result = 0
		mask = 0

		# let's check every possible positive integer number
		for i in range(31, -1, -1):

			# mask start from most significant bit-1,
			# 01000...00,->01100...00,->>>>>> 01111...11
			mask = mask | (1 << i)

			# we have already had a result, just make result's
			# effective bit position extend to right one more
			# for example: 0110100..00 is result, let's check if 0110110..00
			# is the result
			# let's check if the candidateResult is possible?
			# (candidateResult as a result candidate)
			candidateResult = result | (1 << i)

			# record all prefixes(we only need to operate
			# the specific bit positions)
			s = set()
			for num in nums:
				s.add(num & mask)

			# let's check every prefix
			for prefix in s:

				# so..if candidateResult is the existed result,
				# how could that happen?
				# the tricky viewpoint is:
				# A^B = candidateResult <=> B^candidateResult = A
				if (candidateResult ^ prefix) in s:

					# it is possible, so store this result
					result = candidateResult
					break

		return result


# Driver code
if __name__ == '__main__':
	set_ = [9, 8, 5]
	print("Max subset XOR is ", Solution.findMaximumXOR(set_))
