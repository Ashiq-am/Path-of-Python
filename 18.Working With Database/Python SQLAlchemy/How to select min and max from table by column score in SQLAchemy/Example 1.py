from sqlalchemy import create_engine

user , password , host , database = 'root' , '123' , 'localhost' , 'geeksforgeeks'
engine = create_engine(url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'players'

result = connection.execute(f'SELECT MIN(score) , MAX(score) FROM {table_name}')

min_value = None
max_value = None

for elem in result:
	min_value = elem[0]
	max_value = elem[1]

print('Min value : ',min_value)
print('Max value : ',max_value)
