# import threading and time module.
import threading
import time

def print_GFG():
	for i in range(5):
		# suspend the current thread.
		time.sleep(1)
		print("GFG")

def print_Geeksforgeeks():
	for i in range(5):
		# suspend the current thread.
		time.sleep(1.5)
		print("Geeksforgeeks")

# two threads are available in this program.
t1 = threading.Thread(target=print_GFG)
t2 = threading.Thread(target=print_Geeksforgeeks)
t1.start()
t2.start()
