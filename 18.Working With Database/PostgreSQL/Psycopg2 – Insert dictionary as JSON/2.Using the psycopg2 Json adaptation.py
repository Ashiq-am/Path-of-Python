import psycopg2
from psycopg2.extras import Json


# CREATE A PSYCOPG2 CONNECTION
conn = psycopg2.connect(**{
	"database" : "geeks",
	"user"	 : "postgres",
	"password" : "password",
	"host"	 : "localhost",
	"port"	 : 5432,
})

# CREATE DICT OBJECT TO BE INSERTED TO DB
dict_obj = {
	"name": "Suhas Hegde",
	"skill": "PL/SQL",
	"experience": 3
}

# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()

# EXECUTE THE INSERT QUERY
curr.execute(f'''
	INSERT INTO
		json_table(id, json_col)
	VALUES
		('JSON002', %s)
''', [Json(dict_obj)])

# COMMIT THE REQUESTS IN QUEUE
conn.commit()

# CLOSE THE CONNECTION
conn.close()
