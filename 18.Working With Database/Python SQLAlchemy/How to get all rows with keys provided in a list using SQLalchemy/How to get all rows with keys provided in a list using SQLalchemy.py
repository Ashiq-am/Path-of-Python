from sqlalchemy import create_engine

user , password , host , database = 'root' , '123' , 'localhost' , 'geeksforgeeks'
engine = create_engine(url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'student'
keys = ['name','class','dob']

keys_joined = ",".join(keys)
query = f'SELECT {keys_joined} FROM {table_name}'

result = connection.execute(query)
for elem in result:
	print(elem)
