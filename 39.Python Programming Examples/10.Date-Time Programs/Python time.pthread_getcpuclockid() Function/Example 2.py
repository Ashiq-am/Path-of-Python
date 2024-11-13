from threading import Thread
import time

class Hello(Thread):
	def run(self):
		print("thread 1")


helloobj = Hello()
helloobj.start()
print(time.pthread_getcpuclockid(helloobj.ident))
