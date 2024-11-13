class FahrenheitToCelsiusConverter:
	def convert(self, fahrenheit):
		return (fahrenheit - 32) * 5/9

# Example usage
fahrenheit_value = 77
converter = FahrenheitToCelsiusConverter()
celsius_value = converter.convert(fahrenheit_value)
print(f"{fahrenheit_value} Fahrenheit is equal to {celsius_value} Celsius")
