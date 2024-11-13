import struct

def hex_to_float_manual(hex_str):
    int_value = int(hex_str, 16)
    byte_array = int_value.to_bytes(4, byteorder='big')
    float_num = struct.unpack('!f', byte_array)[0]
    return float_num

# Example
hex_str = "40490fdb"
print(hex_to_float_manual(hex_str))
