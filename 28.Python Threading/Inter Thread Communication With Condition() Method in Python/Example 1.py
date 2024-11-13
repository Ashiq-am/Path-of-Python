# code
# import modules

import threading
import time

obj1 = threading.Condition()


def task():
    obj1.acquire()


print('addition of 1 to 10 ')
add = 0
for i in range(1, 11):
    add = add + i
print(add)
obj1.release()
print('the condition object is releases now')

t1 = threading.Thread(target=task)
t1.start()
