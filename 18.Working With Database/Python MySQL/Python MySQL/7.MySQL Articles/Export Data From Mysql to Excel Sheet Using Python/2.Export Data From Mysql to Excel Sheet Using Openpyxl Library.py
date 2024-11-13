import pymysql
from openpyxl import Workbook

# Connect to MySQL database
connection = pymysql.connect(host='localhost',
                             user='username',
                             password='password',
                             database='database_name')

# Create a new Excel workbook
wb = Workbook()
ws = wb.active

# Execute SQL query and fetch data
query = "SELECT * FROM table_name"
cursor = connection.cursor()
cursor.execute(query)
data = cursor.fetchall()

# Write data to Excel
for row_index, row_data in enumerate(data, start=1):
    for col_index, cell_data in enumerate(row_data, start=1):
        ws.cell(row=row_index, column=col_index, value=cell_data)

wb.save('output.xlsx')

# Close the connection
connection.close()
