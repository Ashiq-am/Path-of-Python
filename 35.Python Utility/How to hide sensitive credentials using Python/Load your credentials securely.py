# main.py

# 1. Import the config object from decouple.
from decouple import config

# 2. Retrieve the credentials in your code.

# default data-type of returned value is str.
SECRET_KEY = config('SECRET_KEY')

# you can cast the values on the fly.
DEBUG = config('DEBUG', cast=bool)

# provide defaulft value if key is not found.
EMAIL_HOST = config('EMAIL_HOST',
					default='localhost')
EMAIL_USER = config('EMAIL_USER',
					default='gfg')

# if key not found and no default is given,
# it will raise UndefinedValueError.
EMAIL_PASSWORD = config('EMAIL_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT',
					default=25, cast=int)

print('secret_key :', SECRET_KEY)
print('email_host :', EMAIL_HOST)
print('email_user :', EMAIL_USER)
print('email_pass :', EMAIL_PASSWORD)
print('email_port :', EMAIL_PORT, type(EMAIL_PORT))
