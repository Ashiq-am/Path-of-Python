def global_name_error():
	print(unknown_global_name)

def unbound_local():
	local_val = local_val + 1
	print(local_val)

try:
	global_name_error()
except NameError, err:
	print('Global name error:', err)

try:
	unbound_local()
except UnboundLocalError, err:
	print('Local name error:', err)
