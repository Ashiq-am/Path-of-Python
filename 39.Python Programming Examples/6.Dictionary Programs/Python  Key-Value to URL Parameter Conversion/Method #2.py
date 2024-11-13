# Python code to demonstrate working of
# Key-Value to URL Parameter Conversion
# Using urllib.urlencode() ( with dictionary value list )
import urllib

# initializing dictionary
test_dict = {'gfg' : [1, 2, 3]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using urllib.urlencode() ( with dictionary value list )
# Key-Value to URL Parameter Conversion
res = urllib.urlencode(test_dict, doseq = True)

# printing URL string
print("The URL parameter string is : " + str(res))
