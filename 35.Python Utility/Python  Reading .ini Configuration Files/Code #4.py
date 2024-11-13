import os

# Previously read configuration
print (configur.get('installation', 'prefix'))

# Merge in user-specific configuration
print (configur.read(os.path.expanduser('~/.config.ini')))
print (configur.get('installation', 'prefix'))
print (configur.get('installation', 'library'))

print (configur.getboolean('debug', 'log_errors'))
