# import modules
import threading, queue

# setting up a queue for threads
q = queue.Queue()

def execute_thread():
	while True:
		th=q.get()
		print(f'task {th} started')
		print(f'task {th} finished')
		q.task_done()

# set up for threads to work
threading.Thread(target = execute_thread,
				daemon = True).start()

# sending task requests
for i in range(5):
	q.put(i)
print("all tasks sent")


# making threads wait until all tasks are done
q.join()
print("all tasks completed")
