''''''



'''Enumerate:
Enumerate is built-in python function that takes input as iterator, list etc and returns a tuple containing index 
and data at that index in the iterator sequence. For example, enumerate(cars), returns a iterator that will 
return (0, cars[0]), (1, cars[1]), (2, cars[2]), and so on.'''



# Accessing items using enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for i, x in enumerate(cars):
	print (x)










"""Below solution also works."""



# Accessing items and indexes enumerate()

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars):
	print (x[0], x[1])





"""We can also directly print returned value of enumerate() to see what it returns."""



# Printing return value of enumerate()

cars = ["Aston" , "Audi", "McLaren "]
print(enumerate(cars))






"""Enumerate takes parameter start which is default set to zero. 
We can change this parameter to any value we like. In the below code we have used start as 1."""


# demonstrating the use of start in enumerate

cars = ["Aston" , "Audi", "McLaren "]
for x in enumerate(cars, start=1):
	print (x[0], x[1])