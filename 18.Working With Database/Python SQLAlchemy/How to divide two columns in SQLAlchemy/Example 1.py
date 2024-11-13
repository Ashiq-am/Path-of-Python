from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'players'
column1 = 'score'
column2 = 'matches_played'
result = connection.execute(f'SELECT {column1} / {column2} FROM {table_name}')

for value in result:
	print("Value : ", value)
