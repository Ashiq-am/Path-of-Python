import multiprocessing

def worker_function():
	try:
		raise Exception("Something went wrong")
	except Exception as e:
		print(f"Exception in worker process: {e}")

if __name__ == "__main__":
	process = multiprocessing.Process(target=worker_function)
	process.start()
	process.join()
