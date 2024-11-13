import ctypes
lib = ctypes.cdll.LoadLibrary(None)

# Get the address of sin() from the C math library
addr = ctypes.cast(lib.sin, ctypes.c_void_p).value
print ("addr : ", addr)
