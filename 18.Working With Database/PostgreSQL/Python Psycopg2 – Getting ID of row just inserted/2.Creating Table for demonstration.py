# This program uses fetchone()
# to get the row ID of the latest
# entry in the table

import psycopg2

def get_connection():
	try:
		return psycopg2.connect(
			database="postgres",
			user="postgres",
			password="password",
			host="127.0.0.1",
			port=5432,
		)
	except:
		return False

# GET THE CONNECTION OBJECT
conn = get_connection()

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()

# EXECUTE THE SQL QUERY
curr.execute('''
	INSERT INTO public.USER(user_name, email)
	VALUES ('Sudha Tiwari', 'sudha@xyz.com')
	RETURNING user_id;
''')

# FETCH THE LATEST USER ID USING THE CURSOR
data = curr.fetchone()
print("User ID of latest entry:", data[0])

# CLOSE THE CONNECTION
conn.close()
