nums = [1, 2, 3]
a = (ctypes.c_double * len(nums))(*nums)
print ("a : ", a)

print ("\na[0] : ", a[0])

print ("\na[1] : ", a[1])

print ("\na[2] : ", a[2])
