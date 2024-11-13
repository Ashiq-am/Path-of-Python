import io

def approach2Fn(bytes_io_object):
	return bytes_io_object.getvalue()

bytes_io_object = io.BytesIO(b'Hello, GeeksforGeeks!')
result = approach2Fn(bytes_io_object)
print(type(bytes_io_object))
print(result)
print(type(result))
