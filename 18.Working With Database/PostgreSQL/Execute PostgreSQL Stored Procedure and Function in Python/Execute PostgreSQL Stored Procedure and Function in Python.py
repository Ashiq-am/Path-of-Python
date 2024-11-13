import psycopg2


def get_sale_benchmark(sale_amount):
    connector = None
    try:
        conn_string = "host='host_name' dbname='database_name'\
						user='user_name' password='your_password'"
        connector = psycopg2.connect(conn_string)
        engine = connector.cursor()

        # call stored procedure
        engine.callproc('get_book_sales', [sale_amount, ])

        print("fechting Book list that has crosssed sales benchmark")
        result = cursor.fetchall()
        for row in result:
            print("Book Id = ", row[0], )
            print("Book Name = ", row[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:

        # closing database connection.
        if connector:
            engine.close()
            connector.close()
            print("PostgreSQL connection is closed")


get_sale_benchmark(500)
