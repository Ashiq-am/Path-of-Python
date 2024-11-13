from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'student'

query = f'SELECT section FROM {table_name} WHERE sno IN (1,2,6) ;'
result = connection.execute(query)

for e in result:
	print(e)
