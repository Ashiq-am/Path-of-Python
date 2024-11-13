# Python3 code to demonstrate working of
# Convert Float to digit list
# using map() + regex expression + findall()
import re

# initialize N
N = 6.456

# printing N
print("The floating number is : " + str(N))

# Convert Float to digit list
# using map() + regex expression + findall()
res = list(map(int, re.findall('\d', str(N))))

# printing result
print("List of floating numbers is : " + str(res))
