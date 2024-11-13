divide = _mod.divide
divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
x = 0
divide(10, 3, x)
