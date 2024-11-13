import struct

def bytes_to_bits_binary(byte_data):
	bits_data = bin(int.from_bytes(byte_data, byteorder='big'))[2:]
	return bits_data

# Example: Convert binary data to bits
binary_data = b'\x01\x02\x03\x04'
bits_result_binary = bytes_to_bits_binary(binary_data)

print(f"Binary data: {binary_data}")
print(f"Equivalent bits: {bits_result_binary}")
