import multiprocessing

def worker_function():
	raise Exception("Something went wrong")

if __name__ == "__main__":
	process = multiprocessing.Process(target=worker_function)
	process.start()
	process.join()
process.exit() # Incorrect usage causing AttributeError
