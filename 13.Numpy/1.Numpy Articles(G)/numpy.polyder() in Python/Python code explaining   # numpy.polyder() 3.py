from lib2to3.fixer_util import p1, p2

from pandas import np

a = np.polyder(p1, 1)
b = np.polyder(p2, 1)
print ("\n\nUsing polyder")
print ("p1 derivative of order = 1 : \n", a)
print ("p2 derivative of order = 1 : \n", b)
