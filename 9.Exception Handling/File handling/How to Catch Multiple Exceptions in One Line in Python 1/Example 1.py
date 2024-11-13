a = 1
strs = "hello"

def func(a):
	res = a + strs
	print(res)

try:
	func(a)
except(TypeError)as e:
	print(e)
except(UnboundLocalError) as e:
	print(e)
