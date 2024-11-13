import io

def approach3Fn(bytes_io_object):
	return bytes_io_object.getbuffer().tobytes()

bytes_io_object = io.BytesIO(b'Hello, GeeksforGeeks!')
result = approach3Fn(bytes_io_object)
print(type(bytes_io_object))
print(result)
print(type(result))
