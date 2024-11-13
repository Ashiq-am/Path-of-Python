import psycopg2

# declare the connection string specifying
# the host name database name use name
# and password
conn_string = "host='host_name' dbname='database_name'\
user='user_name' password='your_password'"

# use connect function to establish the connection
conn = psycopg2.connect(conn_string)
