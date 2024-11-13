# Python code to demonstrate
# return the filtered dictionary
# on certain criteria

from six import iteritems
# Initialising dictionary
ini_dict = {'a':1, 'b':-2, 'c':-3, 'd':7, 'e':0}

# printing initial dictionary
print ("initial lists", str(ini_dict))

# filter dictionary such that no value is greater than 0
result = dict((k, v) for k, v in ini_dict.items() if v >= 0)

print("resultant dictionary : ", str(result))
