import mysql.connector


connection = mysql.connector.connect(
	host='localhost', database='geeksforgeeks',
	user='root', password='shubhanshu')

cursor = connection.cursor()

if connection is not None:
	print('Connected Sucessfully')
else:
	print('Connection Failed')
