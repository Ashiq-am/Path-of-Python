class TemperatureConverter:
	def __init__(self, fahrenheit):
		self.fahrenheit = fahrenheit

	def convert_to_celsius(self):
		celsius = (self.fahrenheit - 32) * 5/9
		return celsius

# Example Usage
temperature_f = 75.5
converter = TemperatureConverter(temperature_f)
result = converter.convert_to_celsius()
print(f"{temperature_f} degrees Fahrenheit is equal to {result:.2f} degrees Celsius.")
