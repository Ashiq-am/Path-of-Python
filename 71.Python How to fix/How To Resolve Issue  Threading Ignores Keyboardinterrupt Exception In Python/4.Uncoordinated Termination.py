import threading
import time

def worker():
	while True:
		print("Thread Working...")
		time.sleep(1)

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print("Main Program Terminated.")
