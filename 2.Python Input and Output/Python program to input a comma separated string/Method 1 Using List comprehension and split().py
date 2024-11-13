# Python program to take a comma
# separated string as input


# Taking input when the numbers
# of input are known and storing
# in different variables

# Taking 2 inputs
a, b = [int(x) for x in input("Enter two values\n").split(', ')]
print("\nThe value of a is {} and b is {}".format(a, b))

# Taking 3 inputs
a, b, c = [int(x) for x in input("Enter three values\n").split(', ')]
print("\nThe value of a is {}, b is {} and c is {}".format(a, b, c))

# Taking multiple inputs
L = [int(x) for x in input("Enter multiple values\n").split(', ')]
print("\nThe values of input are", L)
