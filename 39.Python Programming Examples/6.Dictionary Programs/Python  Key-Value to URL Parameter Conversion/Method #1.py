# Python code to demonstrate working of
# Key-Value to URL Parameter Conversion
# Using urllib.urlencode() ( with tuples )
import urllib

# initializing tuples
test_tuples = (('Gfg', 1), ('is', 2), ('best', 3))

# printing original tuples
print("The original tuples are : " + str(test_tuples))

# Using urllib.urlencode() ( with tuples )
# Key-Value to URL Parameter Conversion
res = urllib.urlencode(test_tuples)

# printing URL string
print("The URL parameter string is : " + str(res))
