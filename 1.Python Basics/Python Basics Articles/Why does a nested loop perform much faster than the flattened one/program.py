# import module
import time


# flattened loop
def loop(n):
    for i in range(n ** 3):
        pass


# nested loop
def nested(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass


for i in range(10, 100, 10):
    start = time.time()
    loop(i)
    print('For flattened loop:', time.time() - start)

    start = time.time()
    nested(i)
    print('For nested loop:', time.time() - start)
    print()
