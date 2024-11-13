# Python program to demonstrate
# userstring


from collections import UserString


d = 12344

# Creating an UserDict
userS = UserString(d)
print(userS.data)


# Creating an empty UserDict
userS = UserString("")
print(userS.data)
