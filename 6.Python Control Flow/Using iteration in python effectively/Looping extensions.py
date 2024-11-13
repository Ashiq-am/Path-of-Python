''''''



'''i) Two iterators for a single looping construct: In this case, a list and dictionary are to be 
used for each iteration in a single looping block using enumerate function. Let us see example.'''




# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

# Single dictionary holds prices of cars and
# its accessories.
# First three items store prices of cars and
# next two items store prices of accessories.
prices = {1:"570000$", 2:"68000$", 3:"450000$",
		4:"8900$", 5:"4500$"}

# Printing prices of cars
for index, c in enumerate(cars, start=1):
	print("Car: %s Price: %s"%(c, prices[index]))

# Printing prices of accessories
for index, a in enumerate(accessories,start=1):
	print ("Accessory: %s Price: %s"\
		%(a,prices[index+len(cars)]))











"""ii) zip function (Both iterators to be used in single looping construct):
This function is helpful to combine similar type iterators(list-list or dict- dict etc,) data items at ith position. 
It uses the shortest length of these input iterators. Other items of larger length iterators are skipped. 
In case of empty iterators, it returns No output.

For example, the use of zip for two lists (iterators) helped to combine a single car and its required accessory."""




# Python program to demonstrate the working of zip

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit",
			"Dolby sound kit"]

# Combining lists and printing
for c, a in zip(cars, accessories):
	print("Car: %s, Accessory required: %s"\
          %(c, a))














'''The reverse of these iterators from zip function is known as unzipping using “*” operator.

Use of enumerate function and zip function helps to achieve an effective extension of iteration logic in python and 
solves many more sub-problems of a huge task or problem.'''




# Python program to demonstrate unzip (reverse
# of zip)using * with zip function

# Unzip lists
l1,l2 = zip(*[('Aston', 'GPS'),
			('Audi', 'Car Repair'),
			('McLaren', 'Dolby sound kit')
		])

# Printing unzipped lists
print(l1)
print(l2)


