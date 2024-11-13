from contextlib import contextmanager

def timeblock(label):
	start = time.perf_counter()
	try:
		yield
	finally:
		end = time.perf_counter()
		print('{} : {}'.format(label, end - start))
