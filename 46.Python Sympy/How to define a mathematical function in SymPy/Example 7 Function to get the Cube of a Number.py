# importing SymPy Library
import sympy

# creating class
class cube(sympy.Function):

    @classmethod
    # defining subclass function with 'eval()' class method
    def eval(cls, x):
        print(x**3)

# calling the function
cube(9)
