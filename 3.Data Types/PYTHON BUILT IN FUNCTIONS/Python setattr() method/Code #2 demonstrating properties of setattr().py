# Python code to demonstrate
# properties of setattr()

# initializing class
class Gfg:
    name = 'GeeksforGeeks'


# initializing object
obj = Gfg()

# printing object before setattr
print("Before setattr name : ", str(obj.name))

# using setattr to assign None to name
setattr(obj, 'name', None)

# using setattr to initialize new attribute
setattr(obj, 'description', 'CS portal')

# printing object after setattr
print("After setattr name : " + str(obj.name))
print("After setattr description : ", str(obj.description))
