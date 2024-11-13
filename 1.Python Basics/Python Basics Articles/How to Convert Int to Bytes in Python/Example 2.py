# declaring an integer value
integer_val = 10

# converting int to bytes with length
# of the array as 5 and byter order as
# little
bytes_val = integer_val.to_bytes(5, 'little')

# printing integer in byte representation
print(bytes_val)
