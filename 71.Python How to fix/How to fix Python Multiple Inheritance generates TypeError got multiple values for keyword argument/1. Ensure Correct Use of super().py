# code
class BaseA:
    def __init__(self, arg1, **kwargs):
        self.arg1 = arg1
        super().__init__(**kwargs)

class BaseB:
    def __init__(self, arg2, **kwargs):
        self.arg2 = arg2
        super().__init__(**kwargs)

class Derived(BaseA, BaseB):
    def __init__(self, arg1, arg2, **kwargs):
        super().__init__(arg1=arg1, arg2=arg2, **kwargs)

# Create an instance of the Derived class
derived = Derived(arg1='value1', arg2='value2')

# Print attributes to verify the correct initialization
print(f"arg1: {derived.arg1}")
print(f"arg2: {derived.arg2}")

# Print Method Resolution Order (MRO)
print("Method Resolution Order (MRO):")
print(Derived.mro())
