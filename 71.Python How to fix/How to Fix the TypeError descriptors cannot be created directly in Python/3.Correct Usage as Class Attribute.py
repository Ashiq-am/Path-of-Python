class MyDescriptor:
    def __get__(self, instance, owner):
        return "value"
class MyClass:
    attr = MyDescriptor()
obj = MyClass()
print(obj.attr)
