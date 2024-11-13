import pandas as pd
import pymysql

connection = pymysql.connect(host='localhost',
                             user='username',
                             password='password',
                             database='database_name')

query = "SELECT * FROM table_name"

data = pd.read_sql(query, connection)

connection.close()

data.to_excel('output.xlsx', index=False)
