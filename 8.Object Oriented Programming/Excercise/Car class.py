import self as self


class Car:
    name = "Ferrari"
    color = "Red"

    def start(self):
        print("Starting the engine")


print("Name of the car:", Car.name)
print("Color:", Car.color)

Car.start(self)
