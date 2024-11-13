import psycopg2


def run():
    try:
        # establishing the connection
        conn = psycopg2.connect(database="root", user='root',
                                password='root', host='127.0.0.1',
                                port='5432')

        # Creating a cursor object using the
        # cursor() method
        cursor = conn.cursor()

        # Executing an query using the execute() method
        cursor.execute('''SELECT * FROM root''')
        print("Connection established to the database root")

        # Closing the connection
        conn.close()
    except:
        print("Connection not established to the database")


# calling the function
run()
