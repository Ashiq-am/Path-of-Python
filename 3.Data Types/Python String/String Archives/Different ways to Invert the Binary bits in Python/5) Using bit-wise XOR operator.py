bit_s = '1010'

# convert binary string
# into integer
temp = int(bit_s, 2)

# applying Ex-or operator
# b/w 10 and 31
inverse_s = temp ^ (2 ** (len(bit_s) + 1) - 1)

# convert the integer result
# into binary result and then
# slicing of the '0b1'
# binary indicator
rslt = bin(inverse_s)[3 : ]

# print the result
print("Inversed string is", rslt )
