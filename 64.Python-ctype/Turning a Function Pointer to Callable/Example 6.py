foo = ctypes.CFUNCTYPE(ctypes.c_double,
					ctypes.c_double,
					ctypes.c_double)(ptr)

print (foo(2, 3))

print ("\n", foo(4, 5))

print ("\n", foo(1, 2))
