class GFGClass:
    class_var = 10


@classmethod
def gfg_class_method(cls):
    print("This is a Class method")
    print(f"Value of class variable {cls.class_var}")


GFGClass.gfg_class_method()
