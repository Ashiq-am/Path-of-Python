# import necessary packages
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# establish connection with the database
engine = create_engine(
	"dialect+driver//username:password@hostname:portnumber/databasename")

# read the postgresql table
table_df = pd.read_sql_table(
	"loan_data",
	con=engine,
	columns=['Loan_ID',
			'Gender',
			'Married',
			'Dependents',
			'Education',
			'Self_Employed',
			'ApplicantIncome',
			'CoapplicantIncome',
			'LoanAmount',
			'Loan_Amount_Term',
			'Credit_History',
			'Property_Area',
			'Loan_Status'],

)

# print the postgresql table loaded as
# pandas dataframe
print(table_df)
