try:
	f = open(filename)
except (FileNotFoundError, PermissionError):
	...
