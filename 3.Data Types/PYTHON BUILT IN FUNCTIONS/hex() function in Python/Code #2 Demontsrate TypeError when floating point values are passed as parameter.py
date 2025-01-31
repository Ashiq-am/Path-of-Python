# hex() accepts only integer vaues as parameters
print("The hexadecimal form of 11.1 is "
							+ hex(11.1))

''' 
# The hexadecimal conversion of floating 
# point integers can be done using the 
# function float.hex() 
print("The hexadecimal form of 11.1 is " 
					+ float.hex(11.1)) 
# Output : 
# The hexadecimal form of 11.1 is 0x1.6333333333333p+3 

# Similarly, float.hex() throws a TypeError 
# when integer values are passed in it. 
'''
