# numeric type
# nothing is passed
z = complex()
print("complex() with no parameters:", z)


# integer type
# passing first parameter only
complex_num1 = complex(5)
print("Int: first parameter only", complex_num1)

# passing both parameters
complex_num2 = complex(7, 2)
print("Int: both parameters", complex_num2)

# float type
# passing first parameter only
complex_num3 = complex(3.6)
print("Float: first parameter only", complex_num3)

# passing both parameters
complex_num4 = complex(3.6, 8.1)
print("Float: both parameters", complex_num4)
print()

# type
print(type(complex_num1))
