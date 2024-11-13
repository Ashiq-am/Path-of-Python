# main.py
import os


def convert(val):
	if type(val) != str:
		return val
	if val.isnumeric():
		return int(val)
	elif val == 'True':
		return True
	elif val == 'False':
		return False
	else:
		return val


secret_key = convert(os.environ.get('SECRET_KEY'))

# gives default value if the credential is absent
google_maps_key = convert(os.environ.get('gmaps_key',
										'mapsapikey543'))
db_user = convert(os.environ.get('DATABASE_USER', 'root'))
db_pass = convert(os.environ.get('DATABASE_PASSWORD', 'pass'))
db_port = convert(os.environ.get('DATABASE_PORT', '3306'))

print('secret_key :', secret_key)
print('google_maps_key :', google_maps_key)
print('db_user :', db_user)
print('db_pass :', db_pass)
print('db_port :', db_port, type(db_port))
