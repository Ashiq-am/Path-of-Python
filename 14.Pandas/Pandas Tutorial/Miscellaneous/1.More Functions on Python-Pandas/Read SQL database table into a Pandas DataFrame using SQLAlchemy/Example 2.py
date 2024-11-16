# import the modules
import pandas as pd
from sqlalchemy import create_engine

# SQLAlchemy connectable
cnx = create_engine('sqlite:///students.db').connect()

# table named 'students' will be returned as a dataframe.
df = pd.read_sql_table('students', cnx)
print(df)
