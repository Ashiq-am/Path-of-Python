import binascii
import struct

def hex_to_float_binascii(hex_str):
    byte_array = binascii.unhexlify(hex_str)
    float_num = struct.unpack('!f', byte_array)[0]
    return float_num

# Example
hex_str = "40490fdb"
print(hex_to_float_binascii(hex_str))
