# Importing the modules
import threading
import sys

# Custom Thread Class
class MyThread(threading.Thread):
	def someFunction(self):
		print("Hello World")
	def run(self):
		self.someFunction()
	def join(self):
		threading.Thread.join(self)

# Driver function
def main():
	t = MyThread()
	t.start()
	t.join()

# Driver code
if __name__ == '__main__':
	main()
