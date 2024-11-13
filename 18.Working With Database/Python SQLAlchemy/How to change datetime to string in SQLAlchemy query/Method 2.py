from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'to_do_list'

query = f'SELECT start_datetime FROM {table_name}'
result = connection.execute(query)

for elem in result:
	value = elem[0]
	print(value, type(value))
	converted_value = str(value)
	print(converted_value, type(converted_value))
	# just a line for much more readable output
	print("____________________________\n")
