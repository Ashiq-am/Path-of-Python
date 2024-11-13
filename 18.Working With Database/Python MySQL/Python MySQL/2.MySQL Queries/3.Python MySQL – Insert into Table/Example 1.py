sql = "INSERT INTO Student (Name, Roll_no) VALUES (%s, %s)"
val = ("Ram", "85")

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "details inserted")

# disconnecting from server
mydb.close()
