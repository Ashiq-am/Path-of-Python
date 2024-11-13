# Returns integer value of '\x00\x10' in big endian machine.
print(int.from_bytes(b'\x00\x10', byteorder ='big'))
