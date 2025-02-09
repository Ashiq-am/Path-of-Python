class Battery:
    def charge(self):
        print("Charging the battery")

class GPS:
    def location(self):
        print("Current location is 123, 456")

class SmartPhone(Battery, GPS):
    pass

# Example usage:
phone = SmartPhone()
phone.charge()
phone.location()
