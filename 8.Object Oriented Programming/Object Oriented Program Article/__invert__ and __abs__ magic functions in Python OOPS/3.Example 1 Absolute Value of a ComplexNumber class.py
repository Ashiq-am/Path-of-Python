class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __abs__(self):
        # Custom implementation for absolute value computation
        return (self.real**2 + self.imag**2)**0.5

# Example usage:
complex_num = ComplexNumber(3, 4)
absolute_value = abs(complex_num)
print(absolute_value)
