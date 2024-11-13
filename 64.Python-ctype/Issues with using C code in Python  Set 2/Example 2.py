import array
arr = array.array('d', [1, 2, 3])
print ("arr : ", arr)

ptr_ = a.buffer_info()
print ("\nptr :", ptr)

print ("\n", ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double)))
