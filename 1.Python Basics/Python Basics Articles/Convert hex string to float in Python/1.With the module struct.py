import struct

def hex_to_float_struct(hex_str):
    hex_str = hex_str.strip().replace("0x", "")
    byte_array = bytes.fromhex(hex_str)
    float_num = struct.unpack('!f', byte_array)[0]
    return float_num

# Example
hex_str = "40490fdb"
print(hex_to_float_struct(hex_str))
