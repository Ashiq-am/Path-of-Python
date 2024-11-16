import pypyodbc as pdb
import pandas as pd

connection = pdb.connect("""
	Driver={{SQL Server Native Client 11.0}};
	Server={0};
	Database={1};
	Trusted_Connection=yes;""".format('LAPTOP-LKHL8PKV',
									'GeeksForGeeks')
)

query = """SELECT * FROM student_marks"""
table = pd.read_sql(query, connection)
print(table)
