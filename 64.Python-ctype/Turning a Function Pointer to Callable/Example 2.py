functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
func = functype(addr)
print ("Function : ", func)
