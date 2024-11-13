# Program to create a table in Oracle database
import cx_Oracle

try:

    con = cx_Oracle.connect('scott/tiger@localhost')

    # Now execute the sqlquery
    cursor = con.cursor()
    cursor.execute("insert into student values(19585, Niranjan Shukla, 72000")

    # commit that insert the provided data
    con.commit()

    print("value inserted successful")

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
