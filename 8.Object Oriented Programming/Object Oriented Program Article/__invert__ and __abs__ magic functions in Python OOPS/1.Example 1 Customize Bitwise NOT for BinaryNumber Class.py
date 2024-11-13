class BinaryNumber:
    def __init__(self, value):
        self.value = value

    def __invert__(self):
        # Custom implementation for bitwise NOT operation
        inverted_value = ~self.value
        return BinaryNumber(inverted_value)


# Example usage:
binary_num = BinaryNumber(5)
inverted_num = ~binary_num
print(inverted_num.value)
