"""Example #1 :"""

# importing numpy module
# it is equivalent to "import numpy"
np = __import__('numpy', globals(), locals(), [], 0)

# array from numpy
a = np.array([1, 2, 3])

# prints the type
print(type(a))







"""Example #2 :"""

# from numpy import complex as comp, array as arr
np = __import__('numpy', globals(), locals(), ['complex', 'array'], 0)

comp = np.complex
arr = np.array







'''Application :
__import__() is not really necessary in everyday Python programming. Its direct use is rare. 
But sometimes, when there is a need of importing modules during the runtime, this function comes quite 
handy.

'''