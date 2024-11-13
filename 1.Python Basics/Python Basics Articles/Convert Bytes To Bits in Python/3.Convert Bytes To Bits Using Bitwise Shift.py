bytes_value3 = b'\b\x16$@P'

bits_value3 = sum(byte << (i * 8) for i, byte in enumerate(reversed(bytes_value3)))

print(bits_value3.bit_length())
