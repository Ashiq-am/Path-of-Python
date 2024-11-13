def producer(q):
	...
	try:
		q.put(item, block = False)
	except queue.Full:
		log.warning('queued item % r discarded !', item)
