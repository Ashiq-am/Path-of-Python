#Python program to demonstrate
#swapping of two numbers
a = 5
b = 1
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1
print("a after swapping: ", a)
print("b after swapping: ", b)
