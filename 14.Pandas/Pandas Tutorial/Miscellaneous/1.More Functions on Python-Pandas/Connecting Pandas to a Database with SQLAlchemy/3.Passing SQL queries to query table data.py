# import necessary packages
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# establish connection with the database
engine = create_engine(
	"dialect+driver//username:password@hostname:portnumber/databasename")

# read table data using sql query
sql_df = pd.read_sql(
	"SELECT * FROM loan_data",
	con=engine
)

print(sql_df)
