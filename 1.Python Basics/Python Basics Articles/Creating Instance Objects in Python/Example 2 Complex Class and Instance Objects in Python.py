class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.mileage = 0

	def drive(self, distance):
		self.mileage += distance


# Creating an instance of the Car class
car_instance = Car("Toyota", "Camry", 2022)

# Accessing and modifying attributes
print(f"{car_instance.make} {car_instance.model} ({car_instance.year})")
car_instance.drive(100)
print(f"Mileage: {car_instance.mileage} miles")
