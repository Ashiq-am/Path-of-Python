_running = True

def consumer(q):
	while _running:
		try:
			item = q.get(timeout = 5.0)
			# Process item
			...
		except queue.Empty:
			pass
