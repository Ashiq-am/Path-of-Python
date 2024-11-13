import struct

binary_data = b'\x40\x49\x0f\xdb'
print(type(binary_data))

int_value = int.from_bytes(binary_data, byteorder='big')
float_value = struct.unpack('>f', int_value.to_bytes(4, byteorder='big'))[0]

print("Float value:", float_value)
print(type(float_value))
