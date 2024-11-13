# Python3 code to demonstrate working
# of uuid3() and uuid5()
import uuid

# initializing a string
url = "https://www.geeksforgeeks.org/fibonacci-sum-subset-elements/"

# using NAMESPACE_URL as namespace
# to generate MD5 hash uuid
print ("The SHA1 hash value generated ID is : ",
			uuid.uuid3(uuid.NAMESPACE_URL, url))

# using NAMESPACE_URL as namespace
# to generate SHA-1 hash uuid
print ("The MD5 hash value generated ID is : ",
			uuid.uuid5(uuid.NAMESPACE_URL, url))
