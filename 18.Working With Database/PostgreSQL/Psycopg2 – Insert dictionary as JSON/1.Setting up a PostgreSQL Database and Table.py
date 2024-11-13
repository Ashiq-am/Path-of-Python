import json
import psycopg2

# SAVE THE DB CONFIG IN A DICT OBJECT
DATABASE_CONFIG = {
	"database": "geeks",
	"user": "postgres",
	"password": "password",
	"host": "localhost",
	"port": 5432,
}


def get_connection():

	# RETURN THE CONNECTION OBJECT
	return psycopg2.connect(
		database=DATABASE_CONFIG.get('database'),
		user=DATABASE_CONFIG.get('user'),
		password=DATABASE_CONFIG.get('password'),
		host=DATABASE_CONFIG.get('host'),
		port=DATABASE_CONFIG.get('port'),
	)


def dict_to_json(value: dict):

	# CONVERT DICT TO A JSON STRING AND RETURN
	return json.dumps(value)


def insert_value(id: str, json_col: str, conn):

	# CREATE A CURSOR USING THE CONNECTION OBJECT
	curr = conn.cursor()

	# EXECUTE THE INSERT QUERY
	curr.execute(f'''
		INSERT INTO
			json_table(id, json_col)
		VALUES
			('JSON001', '{json_col}')
	''')

	# COMMIT THE ABOVE REQUESTS
	conn.commit()

	# CLOSE THE CONNECTION
	conn.close()


def main():

	# CREATE A PSYCOPG2 CONNECTION
	conn = get_connection()

	# CREATE A PYTHON DICT OBJECT FOR JSON COL
	dict_obj = {
		"name": "Amit Pathak",
		"skill": "Python",
		"experience": 4
	}

	# CONVERT DICT OBJECT TO JSON STRING
	json_obj = dict_to_json(value=dict_obj)

	# INSERT VALUES IN THE DATABASE TABLE
	insert_value(id='JSON001', json_col=json_obj,
				conn=conn)

if __name__ == '__main__':
	main()
