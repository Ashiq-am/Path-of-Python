import multiprocessing

def worker_function():
	print("Worker process")

if __name__ == "__main__":
	process = multiprocessing.Process(target=worker_function)
	process.start()
	process.join() # Correctly wait for the process to finish
