def worker():
	while True:
		print("Thread Working...")
		time.sleep(1)

def signal_handler(sig, frame):
	print("Ctrl+C detected. Stopping the thread.")
	sys.exit(0)

# Set up the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

thread = threading.Thread(target=worker)
thread.start()

# Main program can continue or do other tasks if needed
while True:
	time.sleep(1)
