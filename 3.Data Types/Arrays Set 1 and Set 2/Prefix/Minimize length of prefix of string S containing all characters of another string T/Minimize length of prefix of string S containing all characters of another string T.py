# Python3 program for the above approach

def getPrefixLength(srcStr, targetStr):

	# Base Case - if T is empty,
	# it matches 0 length prefix
	if(len(targetStr) == 0):
		return 0

	# Convert strings to lower
	# case for uniformity
	srcStr = srcStr.lower()
	targetStr = targetStr.lower()

	dictCount = dict([])
	nUnique = 0

	# Update dictCount to the
	# letter count of T
	for ch in targetStr:

		# If new character is found,
		# initialize its entry,
		# and increase nUnique
		if(ch not in dictCount):
			nUnique += 1
			dictCount[ch] = 0

		# Increase count of ch
		dictCount[ch] += 1

	# Iterate from 0 to N
	for i in range(len(srcStr)):

		# i-th character
		ch = srcStr[i]

		# Skip if ch not in targetStr
		if(ch not in dictCount):
			continue
		# Decrease Count
		dictCount[ch] -= 1

		# If the count of ch reaches 0,
		# we do not need more ch,
		# and can decrease nUnique
		if(dictCount[ch] == 0):
			nUnique -= 1

		# If nUnique reaches 0,
		# we have found required prefix
		if(nUnique == 0):
			return (i + 1)

	# Otherwise
	return -1


# Driver Code
if __name__ == "__main__":

	S = "MarvoloGaunt"
	T = "Tom"

	print(getPrefixLength(S, T))
