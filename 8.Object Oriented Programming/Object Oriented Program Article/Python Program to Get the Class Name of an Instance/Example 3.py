# class for getting the class name
class test:
    @property
    def cls(self):
        return type(self).__name__


a = test()
print(a.cls)
