# import required modules
import random
import matplotlib.pyplot as plt

# create dataset
year = [i for i in range(1900, 2021)]
GDP = []
for i in range(121):
    GDP.append(random.randint(5, 10))

# display dataset
print("Length of year list is: " + str(len(year)))
print("Length of GDP list is: " + str(len(GDP)))
print("First 10 elements of respective list are: ")
print(year[:10])
print(GDP[:10])
