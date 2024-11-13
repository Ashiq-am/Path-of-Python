from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'players'

column1 = 'score1'
column2 = 'score2'
column3 = 'score3'

result = connection.execute(
	f'SELECT {column1} , {column2} , {column3} FROM {table_name}')

for value in result:
	print("Values of one row :", value)
	sum_value = sum(value)
	print("Sum : ", sum_value)
