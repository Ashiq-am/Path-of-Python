from pandas import np

a = np.polyval([1, 2], 2)
b = np.polyval([4, 9, 5, 4], 2)

print ("\n\nUsing polyval")
print ("p1 at x = 2 : ", a)
print ("p2 at x = 2 : ", b)

c = np.polyval(np.poly1d([4, 9, 5, 4]), np.poly1d(2))
print ("\nc : ", c)
