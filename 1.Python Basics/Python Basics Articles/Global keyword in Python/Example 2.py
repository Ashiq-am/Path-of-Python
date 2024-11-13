# Python program showing to modify
# a global value without using global
# keyword
import a as a

a = 15

# function to change a global value
def change():

	# increment value of a by 5
	a = a + 5
	print(a)

change()
