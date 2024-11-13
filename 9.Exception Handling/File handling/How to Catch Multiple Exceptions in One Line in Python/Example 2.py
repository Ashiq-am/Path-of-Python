a = 1
strs = "hello"

def func(a):
	res: a + strs # unboundlocalerror
	print(res)

try:
	func(a)
except(TypeError, UnboundLocalError) as e:
	print(e)
