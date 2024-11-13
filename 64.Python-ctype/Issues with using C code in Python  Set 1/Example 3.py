# int divide(int, int, int *)
_divide = _mod.divide

_divide.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
_divide.restype = ctypes.c_int

def divide(x, y):
	rem = ctypes.c_int()
	quot = _divide(x, y, rem)
	return quot, rem.value
