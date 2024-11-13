class CelsiusToKelvinConverter:
	def convert(self, celsius):
		return celsius + 273.15

# Example usage
celsius_value = 25
converter = CelsiusToKelvinConverter()
kelvin_value = converter.convert(celsius_value)
print(f"{celsius_value} Celsius is equal to {kelvin_value} Kelvin")
