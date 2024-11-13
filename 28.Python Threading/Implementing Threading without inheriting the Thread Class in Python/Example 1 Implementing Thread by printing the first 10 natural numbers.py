# importing thread module
from threading import *

# class does not extend thread class
class MyThread:
	def display(self):
		i = 0
		print(current_thread().getName())
		while(i <= 10):
			print(i)
			i = i + 1

# creating object of out class
obj = MyThread()

# creating thread object
t = Thread(target = obj.display)

# invoking thread
t.start()
