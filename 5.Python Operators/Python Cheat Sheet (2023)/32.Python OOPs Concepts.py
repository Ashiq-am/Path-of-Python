class Car:
	def __init__(self, make, model, year):
		self._make = make # protected attribute
		self.__model = model # private attribute
		self.year = year # public attribute

	def get_make(self):
		return self._make

	def set_model(self, model):
		self.__model = model

	def get_model(self):
		return self.__model


my_car = Car("Toyota", "Corolla", 2022)

print(my_car.get_make()) # Accessing protected attribute
my_car.set_model("Camry") # Modifying private attribute
print(my_car.get_model()) # Accessing modified private attribute
print(my_car.year) # Accessing public attribute
