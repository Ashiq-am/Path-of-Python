from lib2to3.fixer_util import p1, p2

from pandas import np

a = np.polyder(p1, 2)
b = np.polyder(p2, 2)
print ("\n\nUsing polyder")
print ("p1 derivative of order = 2 : ", a)
print ("p2 derivative of order = 2 : ", b)
