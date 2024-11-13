byte_val = b'\x00\x10'

int_val = int.from_bytes(byte_val, "little")

# printing int object
print(int_val)
