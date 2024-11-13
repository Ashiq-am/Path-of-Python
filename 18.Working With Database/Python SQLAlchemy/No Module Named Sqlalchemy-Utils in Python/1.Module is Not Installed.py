# importing module. But will give error. Module not installed
from sqlalchemy_utils import create_database, database_exists
database_url = 'sqlite:///example.db'
if not database_exists(database_url):
	create_database(database_url)
	print("Database created!")
