bit_s = '1010'

# using ternary operator with
# list comprehension
inverse_s = ''.join(['1' if i == '0' else '0'
					for i in bit_s])

print("Inversed string is", inverse_s)
