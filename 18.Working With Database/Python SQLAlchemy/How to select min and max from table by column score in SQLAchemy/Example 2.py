from sqlalchemy import create_engine

user, password, host, database = 'root', '123', 'localhost', 'geeksforgeeks'
engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'players'

result = connection.execute(f'SELECT score FROM {table_name}')

all_values = []

for elem in result:
	all_values.append(elem[0])

min_value = min(all_values)
max_value = max(all_values)

print('Min value : ', min_value)
print('Max value : ', max_value)
