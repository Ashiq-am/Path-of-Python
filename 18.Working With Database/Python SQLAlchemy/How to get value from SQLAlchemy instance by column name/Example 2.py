from sqlalchemy import create_engine

user, password, host, database =\
'root', '123', 'localhost', 'geeksforgeeks'

engine = create_engine(
	url=f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8')

connection = engine.connect()

table_name = 'student'

# column names whose values we want
column_names = 'name,dob'

# creating the sql query
query = f'SELECT {column_names} FROM {table_name}'

# running the query
result = connection.execute(query)

# fetching all the result and storing in
# values variable
values = result.fetchall()

# printing the output
print(values)
