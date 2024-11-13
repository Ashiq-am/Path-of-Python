# Python program to illustrate memory view

# random bytearray
byte_array = bytearray('XYZ', 'utf-8')

mem_view = memoryview(byte_array)
print(type(mem_view))

string = str(mem_view)
print(type(string))
