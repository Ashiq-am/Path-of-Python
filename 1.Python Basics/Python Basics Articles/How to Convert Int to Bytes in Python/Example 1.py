# declaring an integer value
integer_val = 5

# converting int to bytes with length
# of the array as 2 and byter order as big
bytes_val = integer_val.to_bytes(2, 'big')

# printing integer in byte representation
print(bytes_val)
