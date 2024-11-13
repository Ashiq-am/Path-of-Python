class Descriptor:
    def __get__(self, instance, owner):
        return "value"
class MyClass:
    attr = Descriptor()
obj = MyClass()
print(obj.attr)
