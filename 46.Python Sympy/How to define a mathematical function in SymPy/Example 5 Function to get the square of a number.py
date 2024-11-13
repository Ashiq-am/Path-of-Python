# importing SymPy Library
import sympy


# creating class square
class square(sympy.Function):
    @classmethod
    # defining subclass function with 'eval()' class method
    def eval(cls, x):
        print(x ** 2)


# calling the eval() subclass
# function with integer 4 as its argument
square.eval(4)
