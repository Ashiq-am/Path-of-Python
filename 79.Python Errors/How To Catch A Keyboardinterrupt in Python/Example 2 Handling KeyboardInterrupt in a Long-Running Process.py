import time

def long_running_process():
	try:
		print("Performing a long-running process. Press Ctrl+C to interrupt.")
		for i in range(10):
			time.sleep(1)
			print(f"Processing step {i + 1}")
	except KeyboardInterrupt:
		print("\nInterrupted! Cleaning up before exiting.")
		# Perform cleanup operations here if needed
	finally:
		print("Exiting the program.")

# Call the long_running_process function
long_running_process()
