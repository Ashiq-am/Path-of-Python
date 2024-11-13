# Python program to demonstrate fmean()


from statistics import fmean

# tuple of positive numbers
A1 = (11.4, 3.7, 4, 5, 7.9, 9.4, 2)

# tuple of negative numbers
A2 = (-1.9, -2.8, -4, -7.5, -12.2, -19)

# tuple of a mixed range of numbers
A3 = (-1.9, -13.8, -6, 4.2, 5.9, 9.1)

# dictionary of a set of values
# keys are taken in consideration by fmean()
A4 = {1.1: "one.one", 2.8: "two.eight", 3: "three"}

# Printing the mean of A1, A2, A3, A4
print("Floating Point Mean of A1 is", fmean(A1))
print("Floating Point Mean of A2 is", fmean(A2))
print("Floating Point Mean of A3 is", fmean(A3))
print("Floating Point Mean of A4 is", fmean(A4))
