import mysql.connector


# Convert images or files data to binary format
def convert_data(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return binary_data


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='geeksforgeeks',
                                         user='root',
                                         password='shubhanshu')
    cursor = connection.cursor()
    # create table query
    create_table = """CREATE TABLE demo(id INT PRIMARY KEY,\ 
	name VARCHAR (255) NOT NULL, profile_pic BLOB NOT NULL, \ 
	imp_files BLOB NOT NULL) """

    # Execute the create_table query first
    cursor.execute(create_table)
    # printing successful message
    print("Table created Successfully")

    query = """ INSERT INTO demo(id, name, profile_pic, imp_files)\ 
	VALUES (%s,%s,%s,%s)"""

    # First Data Insertion
    student_id = "1"
    student_name = "Shubham"
    first_profile_picture = convert_data("D:\GFG\images\shubham.png")
    first_text_file = convert_data('D:\GFG\details1.txt')

    # Inserting the data in database in tuple format
    result = cursor.execute(
        query, (student_id, student_name, first_profile_picture, first_text_file))
    # Commiting the data
    connection.commit()
    print("Successfully Inserted Values")

# Print error if occured
except mysql.connector.Error as error:
    print(format(error))

finally:

    # Closing all resources
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
