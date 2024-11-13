# create a dictionary
b_dict = {'0': '1', '1': '0'}

bit_s = '1010'

inverse_s = ''

for i in bit_s:
    inverse_s += b_dict[i]

print("Inversed string is", inverse_s)
