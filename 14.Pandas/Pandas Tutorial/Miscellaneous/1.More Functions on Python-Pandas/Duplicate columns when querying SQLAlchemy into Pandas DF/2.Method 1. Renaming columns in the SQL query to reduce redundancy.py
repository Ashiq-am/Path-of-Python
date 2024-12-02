from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import pandas as pd

# Step 1: Set up SQLAlchemy engine for an in-memory SQLite database
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite database

# Step 2: Define the schema (metadata) for the tables
metadata = MetaData()

# Define the 'users' table
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String))

# Define the 'purchases' table (instead of orders)
purchases = Table('purchases', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer),
                  Column('purchase_date', String))

# Step 3: Create the tables in the database
metadata.create_all(engine)

# Step 4: Insert sample data into the tables
with engine.connect() as conn:
    conn.execute(users.insert(), [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ])
    conn.execute(purchases.insert(), [
        {'id': 1, 'user_id': 1, 'purchase_date': '2024-01-01'},
        {'id': 2, 'user_id': 2, 'purchase_date': '2024-02-01'}
    ])
    conn.commit()

# Step 5: Query data from both tables, renaming columns to avoid duplication
query = """
SELECT users.id AS user_id, users.name, purchases.id AS purchase_id, purchases.purchase_date
FROM users
JOIN purchases ON users.id = purchases.user_id
"""

# Step 6: Load the query result into a Pandas DataFrame
with engine.connect() as conn:
    df = pd.read_sql(query, conn)

# Display the result
print(df)