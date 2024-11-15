# program to create class dynamically

# constructor
def constructor(self, arg):
    self.constructor_arg = arg


# method
def displayMethod(self, arg):
    print(arg)


# class method
@classmethod
def classMethod(cls, arg):
    print(arg)


# creating class dynamically
Geeks = type("Geeks", (object,), {
    # constructor
    "__init__": constructor,

    # data members
    "string_attribute": "Geeks 4 geeks !",
    "int_attribute": 1706256,

    # member functions
    "func_arg": displayMethod,
    "class_func": classMethod
})

# creating objects
obj = Geeks("constructor argument")
print(obj.constructor_arg)
print(obj.string_attribute)
print(obj.int_attribute)
obj.func_arg("Geeks for Geeks")
Geeks.class_func("Class Dynamically Created !")
