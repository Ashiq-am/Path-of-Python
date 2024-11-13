def bytes_to_bits(byte_value):
	bits_value = byte_value * 8
	return bits_value

# Example: Convert 4 bytes to bits
bytes_value = 4
bits_result = bytes_to_bits(bytes_value)

print(f"{bytes_value} bytes is equal to {bits_result} bits.")
