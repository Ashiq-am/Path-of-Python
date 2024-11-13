from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'students'

query = f'ALTER TABLE {table_name} CHANGE sno id INT;'
connection.execute(query)
