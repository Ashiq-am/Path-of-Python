import psycopg2.pool

# Create a connection pool with a minimum of 2 connections and
#a maximum of 3 connections
pool = psycopg2.pool.SimpleConnectionPool(
	2, 3, user='postgres', password='test123',
	host='localhost', port='5432', database='test')
