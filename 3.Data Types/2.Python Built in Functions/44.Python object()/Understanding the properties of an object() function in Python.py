class example():
	a = "Geeks"

# declaring the objects of class object
obj1 = demo()
obj2 = demo()

# checking for object equality
print("Is obj1 equal to obj2 : " + str(obj1 == obj2))

# checking for subclass
print("The Example class is a subclass of the object class? ", issubclass(example, object))

# checking for object instance
print("The obj1 is a instance of the object class? ", isinstance(obj1, object))

# trying to add attribute to object
print("Default attribute: ", obj1.a)
obj1.a = "GeeksforGeeks"
print("Assigning new attribute: ", obj1.a)
