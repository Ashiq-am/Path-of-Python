def mean(a,b):
	try:
		print((a+b)/2)
	except TypeError:
		print("wrong data types. enter numeric")


def square(sq):
	try:
		print(sq*sq)
	except TypeError:
		print("wrong data types. enter numeric")


def divide(l,b):
	try:
		print(b/l)
	except TypeError:
				print("wrong data types. enter numeric")
mean(4,5)
square(21)
divide(8,4)
divide("two","one")
