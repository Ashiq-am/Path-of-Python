# import packages
import psycopg2

try:
    # establish a connection to the database
    connection = psycopg2.connect(
        database="SuperMart", user='postgres',
        password='PASS', host='127.0.0.1', port='5432')

    # disable autocommit mode
    connection.autocommit = False

    # creating a cursor object
    cursor = connection.cursor()

    # querying data
    query = """select sales from sales where\
	Order_ID = 'CA-2016-152156'"""
    cursor.execute(query)
    record = cursor.fetchall()
    sum = 0
    for i in record:
        sum = sum + i[0]
    print("total sales from the order id CA-2016-152156 is : " + str(sum))

    # commiting changes
    connection.commit()
    print("succesfully finished the transaction ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error in transaction, reverting all changes using rollback ", error)
    connection.rollback()

finally:

    # closing database connection.
    if connection:
        # closing connections
        cursor.close()
        connection.close()
        print("PostgreSQL database connection is closed")
