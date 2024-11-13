# import module
from threading import *

def fun_daemon():

    print("GFG")

thread_1 = Thread(target=fun_daemon)
print(thread_1.isDaemon())
thread_1.start()
print(thread_1.daemon)
