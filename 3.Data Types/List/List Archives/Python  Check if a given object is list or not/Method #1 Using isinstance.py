# Python code to demonstrate
# check whether the object
# is a list or not

# initialisation list
ini_list1 = [1, 2, 3, 4, 5]
ini_list2 = '12345'

# code to check whether
# object is a list or not
if isinstance(ini_list1, list):
    print("your object is a list !")
else:
    print("your object is not a list")

if isinstance(ini_list2, list):
    print("your object is a list")
else:
    print("your object is not a list")
