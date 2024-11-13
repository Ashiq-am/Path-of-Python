# conversion using floor and ceil .

# importing math module
import math

num = 5.6

floor_value = math.floor(num)

ceil_value = math.ceil(num)

print("the result using floor() : ",
	floor_value ,
	', type : ',type(floor_value).__name__)

print("the result using ceil() : ",
	ceil_value,
	', type: ', type(ceil_value).__name__)
