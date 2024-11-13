# complex number
c = complex(5+9j)

# without format() method
print("Without format() - Imaginary :", str(c.imag), " Real :", str(c.real))

# with format() method
print("With format() - Imaginary : {} Real : {}".format(c.imag, c.real))
