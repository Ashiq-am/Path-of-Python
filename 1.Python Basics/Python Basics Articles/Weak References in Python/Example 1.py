# importing weakref module
import weakref

# creating a class
class GFG(list):
	pass

# creating object of a class
obj = GFG("Geeks")

# creating a normal list object
normal_list = obj
print(f"This is a normal object: {normal_list}")

# this returns a weak reference to obj
weak_list = weakref.ref(obj)
weak_list_obj = weak_list()
print(f"This is a object created using weak reference: {weak_list_obj}")

# creating a proxy of original object
proxy_list = weakref.proxy(obj)
print(f"This is a proxy object: {proxy_list}")

# printing the count of weak references
for objects in [normal_list, weak_list_obj, proxy_list]:
	print(f"Number of weak references: {weakref.getweakrefcount(objects)}")
