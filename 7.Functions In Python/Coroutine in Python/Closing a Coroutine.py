# Python3 program for demonstrating
# closing a coroutine

def print_name(prefix):
	print("Searching prefix:{}".format(prefix))
	try :
		while True:
				name = (yield)
				if prefix in name:
					print(name)
	except GeneratorExit:
			print("Closing coroutine!!")

corou = print_name("Dear")
corou.__next__()
corou.send("Atul")
corou.send("Dear Atul")
corou.close()








"""Coroutine might run indefinitely, to close coroutine close() method is used.
When coroutine is closed it generates GeneratorExit exception which can be catched in usual way.
After closing coroutine, if we try to send values, it will raise StopIteration exception"""