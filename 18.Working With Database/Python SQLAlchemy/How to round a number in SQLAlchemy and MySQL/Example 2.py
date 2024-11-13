from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'students'
col_to_round = 'marks'

query = f'SELECT {col_to_round} FROM {table_name}'

result = connection.execute(query)
for elem in result:
	value = elem[0]
	rounded_value = round(value)
	print("Value :", value, "\t Rounded value :", rounded_value)
