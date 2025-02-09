class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Example usage:
my_car = Car("Toyota", "Corolla", 2021)
my_car.display_details()
