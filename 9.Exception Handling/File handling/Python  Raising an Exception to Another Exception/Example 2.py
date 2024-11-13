try:
	example()
except RuntimeError as e:
	print("It didn't work:", e)
	if e.__cause__:
		print('Cause:', e.__cause__)
