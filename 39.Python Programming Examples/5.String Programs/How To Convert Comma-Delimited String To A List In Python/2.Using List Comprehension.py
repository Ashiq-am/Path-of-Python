#string
cars = "Porsche, G Wagon, Mercedes, Audi, Range Rover"

#list comprehension
cars = [i.strip() for i in cars.split(',')]

print(cars)
