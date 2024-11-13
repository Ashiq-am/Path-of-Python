# Python3 code to demonstrate working of
# Split each word into percent segment in list
# Using join()

# initializing string
test_str = 'geeksforgeeks is best for all geeks and cs students'

# printing original string
print("The original string is : " + str(test_str))

# initializing percent split
per_splt = 50

test_str = test_str.split()

# one liner solution using join()
res = ' '.join([ele[:int((per_splt/100) * len(ele))]
				+ " " + ele[int((per_splt/100) * len(ele)):]
				for ele in test_str])

# printing result
print("Segmented words : " + str(res))
