# import required modules
import time
import psycopg2
import pandas


# connect to server and load SQL database
db = psycopg2.connect(database="postgres",
					user="postgres",
					password="12345",
					host="127.0.0.1",
					port="5432")
cur = db.cursor()

# load pandas dataset
df = pandas.read_csv('gfg.csv')


print('\nUsing PostgreSQL:')

# computing time taken by PostgreSQL
begin = time.time()
print('Sorting data...')
cur.execute("SELECT * FROM gfg order by ESTABLISHED")
print(cur.fetchall())
end = time.time()
print('Time Taken:', end-begin)


print('\nUsing Pandas:')

# computing time taken by Pandas
begin = time.time()
print('Sorting data...')
df.sort_values(by=['ESTABLISHED'], inplace=True)
print(df)
end = time.time()
print('Time Taken:', end-begin)
