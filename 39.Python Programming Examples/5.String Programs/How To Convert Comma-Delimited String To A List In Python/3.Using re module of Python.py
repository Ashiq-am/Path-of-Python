#import the re module
import re

#string
cars = "Porsche, G Wagon, Mercedes, Audi, Range Rover"

#regex/regular expression
cars = re.split(r'\s*,\s*', cars)

print(cars)
