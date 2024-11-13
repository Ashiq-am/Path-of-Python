# Python code to demonstrate
# to get characters in string
import re

# initialising string
ini_string = "123()#$ABGFDabcjw"
ini_string2 = "abceddfgh"

# printing strings
print ("initial string : \n", ini_string, "\n", ini_string2)

# code to find characters in string
res1 = " ".join(re.findall("[a-zA-Z]+", ini_string))
res2 = " ".join(re.findall("[a-zA-Z]+", ini_string2))

# printing resultant string
print ("first string result: ", str(res1))
print ("second string result: ", str(res2))
