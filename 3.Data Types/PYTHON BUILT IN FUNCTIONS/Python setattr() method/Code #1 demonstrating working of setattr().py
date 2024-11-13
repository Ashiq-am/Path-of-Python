# Python code to demonstrate
# working of setattr()

# initializing class
class Gfg:
    name = 'GeeksforGeeks'


# initializing object
obj = Gfg()

# printing object before setattr
print("Before setattr name : ", obj.name)

# using setattr to change name
setattr(obj, 'name', 'Geeks4Geeks')

# printing object after setattr
print("After setattr name : ", obj.name)
