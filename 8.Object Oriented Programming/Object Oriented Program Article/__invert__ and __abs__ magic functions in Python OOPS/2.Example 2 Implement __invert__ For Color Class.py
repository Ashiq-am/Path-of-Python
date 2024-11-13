class Color:
    def __init__(self, rgb):
        self.rgb = rgb

    def __invert__(self):
        # Custom implementation for bitwise NOT operation
        inverted_rgb = tuple(255 - value for value in self.rgb)
        return Color(inverted_rgb)


# Example usage:
original_color = Color((100, 150, 200))
inverted_color = ~original_color
print(inverted_color.rgb)
