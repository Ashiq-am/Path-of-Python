class Car():

    # constructor
    def __init__(self, company, modelName, price, seatingCapacity):
        self.company = company
        self.modelName = modelName
        self.price = price
        self.seatingCapacity = seatingCapacity


# list of car objects
carsList = [Car('Honda', 'Jazz', 900000, 5),
            Car('Suziki', 'Alto', 450000, 4),
            Car('BMW', 'X5', 9000000, 5)]

# cars with price less than 10 Lakhs
economicalCars = [car for car in carsList if car.price <= 1000000]

# print those cars
for car in economicalCars:
    print(car.company + '--' + car.modelName)
