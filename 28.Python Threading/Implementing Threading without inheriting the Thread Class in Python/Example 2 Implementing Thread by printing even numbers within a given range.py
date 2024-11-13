# importing thread module
from threading import *

# class does not extend thread class
class MyThread:
	def display(self):
		i = 10
		j = 20
		print(current_thread().getName())
		for num in range(i, j + 1):
			if(num % 2 == 0):
				print(num)

# creating an object of our class
obj = MyThread()

# creating a thread object
t = Thread(target = obj.display)

# invoking the thread
t.start()
