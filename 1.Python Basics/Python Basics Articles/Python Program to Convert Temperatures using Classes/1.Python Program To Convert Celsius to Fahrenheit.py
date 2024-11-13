class CelsiusToFahrenheitConverter:
	def convert(self, celsius):
		return (celsius * 9/5) + 32

# Example usage
celsius_value = 25
converter = CelsiusToFahrenheitConverter()
fahrenheit_value = converter.convert(celsius_value)
print(f"{celsius_value} Celsius is equal to {fahrenheit_value} Fahrenheit")
