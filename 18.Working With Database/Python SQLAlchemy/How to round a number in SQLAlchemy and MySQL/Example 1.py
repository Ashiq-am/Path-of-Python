from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'students'
col_to_round = 'marks'

query = f'SELECT ROUND({col_to_round}) FROM {table_name}'

result = connection.execute(query)
for elem in result:
	print(elem[0])
