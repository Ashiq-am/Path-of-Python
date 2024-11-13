# Python program to demonstrate the working of zip

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit",
			"Dolby sound kit"]

# Combining lists and printing
for c, a in zip(cars, accessories):
	print("Car: %s, Accessory required: %s"%(c, a))
