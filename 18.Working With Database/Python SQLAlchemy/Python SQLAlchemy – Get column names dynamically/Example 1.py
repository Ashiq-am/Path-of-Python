from sqlalchemy import create_engine

table_name = 'student'

engine = create_engine("mysql+pymysql://root:root123@localhost/geeksforgeeks")
connection = engine.connect()

result = connection.execute(f"SELECT * FROM {table_name}")

print(result.keys())
