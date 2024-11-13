import psycopg2

# Connection to the PostGreSql database
connection = psycopg2.connect(
	host="localhost",
	database="example",
	user="postgres",
	password="samexp"
)

# Creation of a cursor object
cursor = connection.cursor()

# Define the update statement with placeholders for dynamic data
update="UPDATE details SET firstname = %s, lastname = %s, age = %s WHERE email = %s"

data=[]

n=int(input("Enter n: "))

for i in range(n):
	print("User - ",i," details: ")
	email=input("Email: ")
	fn=input("First name: ")
	ln=input("Last name: ")
	age=int(input("Age: "))

	tup=(fn,ln,age,email)
	data.append(tup)

# Execute the update statement for each row of data
for row in data:
	cursor.execute(update,row)

# Commit the changes to the database
connection.commit()
print("completed")

# Close the cursor and database connection
cursor.close()
connection.close()
