# demonstrating the use of start in enumerate

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars, start=1):
	print (x[0], x[1])
