from array import *

def Product(arr):
	p = 1
	for i in arr:
		p *= i
	print("Product: ", p)

arr = array('f', [4.1, 5.2, 6.3])
Product(arr)
