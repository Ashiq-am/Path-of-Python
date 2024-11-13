backup_dbname = db + '_backup'
try:
	cursor.execute(f'CREATE DATABASE {backup_dbname}')
except:
	pass
