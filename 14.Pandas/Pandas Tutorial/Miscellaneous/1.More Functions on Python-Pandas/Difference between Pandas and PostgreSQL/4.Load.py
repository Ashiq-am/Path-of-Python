# import required modules
import time
import psycopg2
import pandas


print('\nUsing PostgreSQL:')

# computing time taken by PostgreSQL
begin = time.time()
# connect to server and load SQL database
print('Loading SQL dataset...')
db = psycopg2.connect(database="postgres",
					user="postgres",
					password="12345",
					host="127.0.0.1",
					port="5432")
cur = db.cursor()
end = time.time()
print('Time Taken:', end-begin)


print('\nUsing Pandas:')

# computing time taken by Pandas
begin = time.time()
print('Loading pandas dataset...')
# load pandas dataset
df = pandas.read_csv('gfg.csv')
end = time.time()
print('Time Taken:', end-begin)
