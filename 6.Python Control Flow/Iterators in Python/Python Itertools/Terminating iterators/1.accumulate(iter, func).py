# Python code to demonstrate the working of
# accumulate()


import itertools
import operator

# initializing list 1
li1 = [1, 4, 5, 7]

# using accumulate()
# prints the successive summation of elements
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

# using accumulate()
# prints the successive summation of elements
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))
