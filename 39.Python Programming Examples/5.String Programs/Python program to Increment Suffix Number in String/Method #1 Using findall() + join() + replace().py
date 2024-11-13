# Python3 code to demonstrate working of
# Increment Suffix Number
# Using findall() + join() + replace()
import re

# initializing string
test_str = 'geeks006'

# printing original string
print("The original string is : " + str(test_str))

# getting suffix number
reg = re.compile(r'[ 0 - 9]')
mtch = reg.findall(test_str)

# getting number
num = ''.join(mtch[-3:])
pre_str = test_str.replace(num, '')

# Increment number
add_val = int(num) + 1

# joining prefix str and added value
res = pre_str + str(add_val)

# printing result
print("Incremented numeric String : " + str(res))
