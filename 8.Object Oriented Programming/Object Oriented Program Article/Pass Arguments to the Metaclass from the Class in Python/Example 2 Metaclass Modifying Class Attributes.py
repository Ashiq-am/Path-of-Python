class MyMeta(type):
    def __new__(cls, name, bases, class_dict, prefix):
        # Modify class attributes based on the passed prefix
        for key, value in class_dict.items():
            if isinstance(value, str):
                class_dict[key] = prefix + value

        # Call the parent metaclass's __new__ method
        return super().__new__(cls, name, bases, class_dict)


class MyClass(metaclass=MyMeta, prefix="Hello_"):
    message = "World"
    another_message = "Python"

    def greet(self):
        return self.message


# Instantiate the class
my_instance = MyClass()

# Access modified attributes
print(my_instance.message)
print(my_instance.another_message)
print(my_instance.greet())
