from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'student'

query = f'SELECT name FROM {table_name};'
result = connection.execute(query)

values = []
for e in result:
	values.append(e[0])

print(values)
