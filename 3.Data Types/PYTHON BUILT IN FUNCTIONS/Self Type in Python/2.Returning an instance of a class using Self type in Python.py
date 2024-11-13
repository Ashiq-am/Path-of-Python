# Import Self
from typing import Self

# Define a base class
class Car:
	def set_brand(self,
				brand: str) -> Self:
		self.brand = brand
		return self

# Define a child class
class Brand(Car):
	def set_speed(self,
				speed: float) -> Self:
		self.speed = speed
		return self

# Calling object inside print statement
print(Car().set_brand("Maruti"))
print(Brand().set_brand("Mar\
uti").set_speed(110.5))
print(type(Car().set_brand("Maruti")))
print(type(Brand().set_brand("Maruti").set_speed(110.5)))
