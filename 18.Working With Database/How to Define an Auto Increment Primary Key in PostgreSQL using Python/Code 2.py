import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="testdb")

    cursor = connection.cursor()

    # As Employee table is having auto incremented primary id column(employee_id), no need to specify about that value here
    postgres_insert_query = ''' INSERT INTO EMPLOYEE (FIRST_NAME, LAST_NAME, AGE,SEX,INCOME) VALUES (%s,%s,%s,%s,%s)'''
    record_to_insert = ('asd', 'wer', 19, 'f', 5000)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into Employee table")

except (Exception, psycopg2.Error) as error:
    if (connection):
        print("Failed to insert record into Employee table", error)

finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
