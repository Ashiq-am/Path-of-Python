import signal
import time

def handler(signum, frame):
	print("Received termination signal")
	raise SystemExit("Exiting due to signal")

signal.signal(signal.SIGINT, handler)

try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print("KeyboardInterrupt received")
