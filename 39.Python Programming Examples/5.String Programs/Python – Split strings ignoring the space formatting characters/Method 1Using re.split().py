# Python3 code to demonstrate working of
# Split Strings igoring Space charaters
# Using re.split()
import re

# initializing string
test_str = 'geeksforgeeks\n\r\t\t\nis\t\tbest\r\tfor geeks'

# printing original string
print("The original string is : " + str(test_str))

# space regex with split returns the result
res = re.split(r'[\n\t\f\v\r ]+', test_str)

# printing result
print("The split string : " + str(res))
