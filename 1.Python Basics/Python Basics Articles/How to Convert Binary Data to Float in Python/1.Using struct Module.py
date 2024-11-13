import struct

# binary data
binary_data = b'\x40\x49\x0f\xdb'
print(type(binary_data))

# Cast binary data to float
float_value = struct.unpack('>f', binary_data)[0]
print("Float value:", float_value)
print(type(float_value))
