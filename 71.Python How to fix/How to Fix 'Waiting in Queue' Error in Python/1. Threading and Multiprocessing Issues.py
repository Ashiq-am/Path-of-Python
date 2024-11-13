import threading
import queue
import time

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f'Processing item: {item}')
        time.sleep(1)
        q.task_done()

q = queue.Queue()
threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

for item in range(20):
    q.put(item)

q.join()

for i in range(5):
    q.put(None)

for t in threads:
    t.join()
