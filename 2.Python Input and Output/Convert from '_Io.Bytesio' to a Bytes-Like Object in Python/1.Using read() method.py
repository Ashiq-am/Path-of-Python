import io

def approach1Fn(bytes_io_object):
	return bytes_io_object.read()

bytes_io_object = io.BytesIO(b'Hello, GeeksforGeeks!')
result = approach1Fn(bytes_io_object)
print(type(bytes_io_object))
print(result)
print(type(result))
