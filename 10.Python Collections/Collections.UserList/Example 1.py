# Python program to demonstrate
# userlist


from collections import UserList


L = [1, 2, 3, 4]

# Creating a userlist
userL = UserList(L)
print(userL.data)


# Creating empty userlist
userL = UserList()
print(userL.data)
