# Python code to find key with
# Maximum value in Dictionary
import operator

# Dictionary Initialization
Car = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}

# Getting max item
keyMax = max(Car.items(), key = operator.itemgetter(1))[0]
print(keyMax)
