# Python 3 program to illustrate
#use of copyreg module
import copyreg, copy, pickle
class C(object):
	def __init__(self, a):
		self.a = a

def pickle_c(c):
	print("pickling a C instance...")
	return C, (c.a, )

copyreg.pickle(C, pickle_c)
c = C(1)
d = copy.copy(c)
print (d)

p = pickle.dumps(c)
print (p)
