# main.py
from secrets import secrets

secret_key = secrets.get('SECRET_KEY')

# gives default value if the credential is absent
google_maps_key = secrets.get('gmaps_key',
							'mapsapikey543')

db_user = secrets.get('DATABASE_USER', 'root')
db_pass = secrets.get('DATABASE_PASSWORD', 'pass')
db_port = secrets.get('DATABASE_PORT', 3306)

print('secret_key :', secret_key)
print('google_maps_key :', google_maps_key)
print('db_user :', db_user)
print('db_pass :', db_pass)

# no need to type cast numbers and booleans
print('db_port :', db_port, type(db_port))
