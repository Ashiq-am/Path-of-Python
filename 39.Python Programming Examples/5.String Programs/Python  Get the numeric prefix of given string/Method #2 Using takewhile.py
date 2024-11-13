# Python code to demonstrate
# to get numeric prefix in string
# if present
from itertools import takewhile

# initialising string
ini_string = "123abcjw"
ini_string2 = "abceddfgh"

# printing string and its length
print ("initial string : ", ini_string, ini_string2)

# code to find numeric prefix in string
res1 = ''.join(takewhile(str.isdigit, ini_string))
res2 = ''.join(takewhile(str.isdigit, ini_string2))

# printing resultant string
print ("first string result: ", res1)
print ("second string result: ", res2)
