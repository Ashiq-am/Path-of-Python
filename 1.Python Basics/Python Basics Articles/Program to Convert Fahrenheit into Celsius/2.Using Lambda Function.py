# using lambda function
fahrenheit_to_celsius = lambda fahrenheit: (fahrenheit - 32) * 0.5556

fahrenheit = 40
celsius = fahrenheit_to_celsius(fahrenheit)
print("Temperature in Celsius:", celsius)
