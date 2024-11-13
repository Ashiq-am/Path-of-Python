# Python code to demonstrate
# to get numeric prefix in string
# if present
import re

# initialising string
ini_string = "123abcjw"
ini_string2 = "abceddfgh"

# printing string and its length
print ("initial string : ", ini_string, ini_string2)

# code to find numeric prefix in string
res1 = re.sub('\D.*', '', ini_string)
res2 = re.sub('\D.*', '', ini_string2)


# printing resultant string
print ("first string result: ", str(res1))
print ("second string result: ", str(res2))
