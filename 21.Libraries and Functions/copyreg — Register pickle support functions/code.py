# Python 3 program to illustrate
# use of copyreg module
import copyreg, copy, pickle

class B(object):
	def __init__(self, a):
		self.a = a

def pickle_b(b):
	print("pickling a C instance...")
	return C, (b.a, )

copyreg.pickle(B, pickle_b)
b = B(1)
d = copy.copy(b)
print (d)

r = pickle.dumps(b)
print (r)
