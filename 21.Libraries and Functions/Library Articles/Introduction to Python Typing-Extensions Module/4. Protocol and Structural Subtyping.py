from typing_extensions import Protocol

class Drivable(Protocol):
    def drive(self) -> None:
        pass

class Car:
    def drive(self) -> None:
        print("Driving a car")

def test_drive(vehicle: Drivable) -> None:
    vehicle.drive()


car = Car()
test_drive(car)
