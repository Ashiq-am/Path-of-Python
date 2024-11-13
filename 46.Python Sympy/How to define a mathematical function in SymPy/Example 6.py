# importing SymPy Library
import sympy


# creating class 'square'
class square(sympy.Function):
    @classmethod
    # defining subclass function with 'eval()' class method
    def eval(cls, x):
        print(x ** 2)


# calling class
square(4)
