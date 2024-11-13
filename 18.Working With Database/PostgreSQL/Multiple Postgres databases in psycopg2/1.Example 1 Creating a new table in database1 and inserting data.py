import psycopg2

# Establishing connection with database1
conn1 = psycopg2.connect(
	database="database1",
	user="username",
	password="password",
	host="localhost",
	port="5432"
)
print("Connection successful!!")

# Creating a new table
cur1 = conn1.cursor()
cur1.execute('''CREATE TABLE employees
				(ID INT PRIMARY KEY NOT NULL,
				NAME TEXT NOT NULL,
				AGE INT NOT NULL,
				ADDRESS TEXT);''')
print("Table created successfully")

# Inserting data
cur1.execute(
	"INSERT INTO employees (ID, NAME, AGE, ADDRESS) VALUES (1, 'John', 30, 'California')")
conn1.commit()
print("Data inserted successfully")

# Closing connection
cur1.close()
conn1.close()
print("Connection Closed!!")
