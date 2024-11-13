# Python3 code to demonstrate
# similarity between strings
# using SequenceMatcher.ratio()
from difflib import SequenceMatcher

# Utility function to compute similarity
def similar(str1, str2):
	return SequenceMatcher(None, str1, str2).ratio()

# Initializing strings
test_string1 = 'Geeksforgeeks'
test_string2 = 'Geeks'

# using SequenceMatcher.ratio()
# similarity between strings
res = similar(test_string1, test_string2)

# printing the result
print ("The similarity between 2 strings is : " + str(res))
