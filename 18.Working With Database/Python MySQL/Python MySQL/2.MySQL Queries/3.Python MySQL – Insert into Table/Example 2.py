sql = "INSERT INTO Student (Name, Roll_no) VALUES (%s, %s)"
val = [("Akash", "98"),
	("Neel", "23"),
	("Rohan", "43"),
	("Amit", "87"),
	("Anil", "45"),
	("Megha", "55"),
	("Sita", "95")]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "details inserted")

# disconnecting from server
mydb.close()
