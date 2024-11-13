if t.is_alive():
	print('Still running')
else:
	print('Completed')


t.join()
