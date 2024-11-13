bit_s = '1010'

# replace "1" with "2"
# output : "2020"
inverse_s = bit_s.replace('1', '2')

# replace "0" with "1"
# output : "2121"
inverse_s = inverse_s.replace('0', '1')

# replace "0" with "1"
# output : "0101"
inverse_s = inverse_s.replace('2', '0')

print("Inversed string is",inverse_s)
