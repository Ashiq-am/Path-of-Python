# import module
from threading import *

def fun():
	print("Geeks For Geeks")

T = Thread(target = fun)

print("GFG")
print(T.isDaemon())

# set thread as Daemon
T.setDaemon(True)

# check status
print(T.isDaemon())
T.start()
