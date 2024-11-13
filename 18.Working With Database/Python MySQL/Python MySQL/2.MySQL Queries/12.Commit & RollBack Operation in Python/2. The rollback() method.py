# Python program to demonstrate
# rollback() method

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    # Connecting to the Database
    mydb = mysql.connector.connect(
        host='localhost',
        database='College',
        user='root',
    )

    cs = mydb.cursor()

    # drop clause
    statement = "UPDATE STUDENT SET AGE = 23 WHERE Name ='Rishi Kumar'"

    cs.execute(statement)

    # commit changes to the database
    mydb.commit()

    # update successful message
    print("Database Updated !")

except mysql.connector.Error as error:

    # update failed message as an error
    print("Database Update Failed !: {}".format(error))

    # reverting changes because of exception
    mydb.rollback()

# Disconnecting from the database
mydb.close()
