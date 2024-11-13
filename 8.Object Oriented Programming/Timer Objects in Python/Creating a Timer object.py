# Program to demonstrate
# timer objects in python

import threading
def gfg():
	print("GeeksforGeeks\n")

timer = threading.Timer(2.0, gfg)
timer.start()
print("Exit\n")









#Create a timer that will run function with arguments args and keyword arguments kwargs,
# after interval seconds have passed. If args is None (the default) then an empty list will be used.
# If kwargs is None (the default) then an empty dict will be used.