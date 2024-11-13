import multiprocessing
import os
import psycopg2


# Our worker function, each process calls to this function
def worker(start, end):
	conn = psycopg2.connect("dbname=test user=postgres password=admin")
	cur = conn.cursor()
	for i in range(start, end):
		cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
					(i, str(chr(i))))
	cur.close()
	# Commit our database changes
	conn.commit()

	# Close our database connection
	conn.close()


if __name__ == '__main__':
	# Create a connection to our database
	conn = psycopg2.connect("dbname=test user=postgres password=admin")

	# Create a preliminary cursor to create a table in the database
	cur = conn.cursor()

	# Create a database table
	cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data text);")

	# Close the cursor and connection
	cur.close()
	conn.commit()
	conn.close()

	# Create our 4 processes
	p1 = multiprocessing.Process(target=worker, args=[1, 32])
	p2 = multiprocessing.Process(target=worker, args=[32, 64])
	p3 = multiprocessing.Process(target=worker, args=[64, 96])
	p4 = multiprocessing.Process(target=worker, args=[96, 128])

	# Start all the processes
	p1.start()
	p2.start()
	p3.start()
	p4.start()

	# Wait until all processes finish
	p1.join()
	p2.join()
	p3.join()
	p4.join()
