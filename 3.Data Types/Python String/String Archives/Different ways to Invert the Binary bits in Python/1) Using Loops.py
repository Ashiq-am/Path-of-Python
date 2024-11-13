bit_s = '1010'
inverse_s = ''

for i in bit_s:

    if i == '0':
        inverse_s += '1'

    else:
        inverse_s += '0'

print("Inversed string is ",inverse_s)
