# Python3 code to demonstrate working
# of uuid3() and uuid5()
import uuid

# initializing a string
qualified_dns = "www.geeksforgeeks.org"

# using NAMESPACE_DNS as namespace
# to find MD5 hash id
print ("The SHA1 hash value generated ID is : ",
	uuid.uuid3(uuid.NAMESPACE_DNS, qualified_dns))

# using NAMESPACE_DNS as namespace
# to generate SHA-1 hash id
print ("The MD5 hash value generated ID is : ",
	uuid.uuid5(uuid.NAMESPACE_DNS, qualified_dns))
