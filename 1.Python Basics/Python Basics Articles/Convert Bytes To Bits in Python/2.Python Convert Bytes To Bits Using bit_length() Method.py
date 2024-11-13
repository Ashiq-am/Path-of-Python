bytes_value1 = b'\x01\x23\x45\x67\x89\xAB\xCD\xEF'

bits_value1 = int.from_bytes(bytes_value1, byteorder='big').bit_length()

print(bits_value1)
