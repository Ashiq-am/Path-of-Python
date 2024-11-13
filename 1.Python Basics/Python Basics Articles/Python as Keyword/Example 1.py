# Python code to demonstrait
# 'as' keyword

# Import ramdom module with alias
import random as geek

# Function showing working of as keyword
def Geek_Func():

	# Using random module with alias
	geek_RandomNumber = geek.randint(5, 10)
	geek_RandomNumber2 = geek.randint(1, 5)

	# Printing our number
	print(geek_RandomNumber)
	print(geek_RandomNumber2)


Geek_Func()
