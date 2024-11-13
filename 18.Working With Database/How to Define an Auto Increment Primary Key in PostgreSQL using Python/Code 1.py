import psycopg2


def create_table():
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(database="testdb", user="postgres",
                                password="password", host="127.0.0.1", port="5432")
        print("Opened database successfully")
        # create a cursor
        cursor = conn.cursor()
        # Droping EMPLOYEE table if already exists.
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

        # Creating table as per requirement, let us have EMPLOYEE table
        # and in order to have auto increment primary key, EMPLOYEE_ID SERIAL PRIMARY KEY
        # is used and it is explained before code
        sql = '''CREATE TABLE EMPLOYEE( 
		EMPLOYEE_ID SERIAL PRIMARY KEY, 
		FIRST_NAME CHAR(20) NOT NULL, 
		LAST_NAME CHAR(20), 
		AGE INT, 
		SEX CHAR(1), 
		INCOME FLOAT 
		)'''
        cursor.execute(sql)
        print("Table created successfully........")

        # close communication with the PostgreSQL database server
        cursor.close()

        # commit the changes
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_table()
