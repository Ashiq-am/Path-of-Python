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

# bmw cars
BMW_Cars = [car for car in carsList if car.company == 'BMW']

# print those cars
for car in BMW_Cars:
    print(car.company + '--' + car.modelName + '--' +
          str(car.price) + '--' + str(car.seatingCapacity))
