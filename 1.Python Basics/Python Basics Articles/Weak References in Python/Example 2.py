# import weakref module
import weakref


# creates a class
class GFG:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)


# creates an object of class GFG
# (consider that this object is very
# large and has been stored in the cache)
value = GFG(5)

# creates a Weak Value Dictionary
weak_dict = weakref.WeakValueDictionary()

# inserting value into the dictionary
weak_dict["num"] = value

# getting the weak ref count
print(f'Weak reference count is: {weakref.getweakrefcount(weak_dict)}')

# deleting the weak dictionary
del weak_dict

# running this will generate error
# print(weak_dict)
