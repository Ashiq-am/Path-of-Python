# Python program to illustrate
# Modifying internal data using memory view

# random bytearray
byte_array = bytearray('XYZ', 'utf-8')
print('Before update:', byte_array)

mem_view = memoryview(byte_array)

# update 2nd index of mem_view to J
mem_view[2]= 74
print('After update:', byte_array)
