from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

class Square(Shape):
	def area(self):
		raise NotImplementedError("area() method not implemented for Square")

# Attempting to instantiate Square and call area()
try:
	square = Square()
	square.area() # This will raise a NotImplementedError
except NotImplementedError as e:
	print("NotImplementedError:", e)
