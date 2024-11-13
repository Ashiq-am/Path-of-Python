try:
	out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], timeout = 5)
except subprocess.TimeoutExpired as e:
	...
