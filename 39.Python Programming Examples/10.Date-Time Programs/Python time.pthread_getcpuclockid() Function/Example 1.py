from threading import Thread

class Hello(Thread):
	def run(self):
		pass
		# code to be executed in this thread

helloobj = Hello()
helloobj.start()
print(helloobj.ident)
