# Python3 code to demonstrate
# how to check whether string contains
# only numbers or not

# Initialising string
ini_string1 = '1234556'
ini_string2 = 'abc123'

# printing initial string
print("Initial Strings : ", ini_string1, ini_string2)

# Using try / exception:
try:
    num = int(ini_string1)
    print("String1 contains only digits")
except:
    print("String1 doesn'tcontains only digits")

try:
    num = int(ini_string2)
    print("String2 contains only digits")
except:
    print("String2 doesn't contains only digits")

