class KelvinToCelsiusConverter:
	def convert(self, kelvin):
		return kelvin - 273.15

# Example usage
kelvin_value = 300
converter = KelvinToCelsiusConverter()
celsius_value = converter.convert(kelvin_value)
print(f"{kelvin_value} Kelvin is equal to {celsius_value} Celsius")
