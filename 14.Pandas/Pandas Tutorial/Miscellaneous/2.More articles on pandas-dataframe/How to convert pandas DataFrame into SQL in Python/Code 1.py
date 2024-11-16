#importing sql library
from sqlalchemy import create_engine

# create a referrence
# for sql library
engine = create_engine('sqlite://', echo = False)

# attach the data frame to the sql
# with a name of the table
# as "Employee_Data"
dataset.to_sql('Employee_Data', con = engine)

# show the complete data
# from Employee_Data table
print(engine.execute("SELECT * FROM Employee_Data").fetchall())
