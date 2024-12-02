from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import pandas as pd

# Step 1: Set up SQLAlchemy engine for an in-memory SQLite database
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite database

# Step 2: Define the schema (metadata) for the tables
metadata = MetaData()

# Define the 'users' table
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('email', String))

# Define the 'orders' table
orders = Table('orders', metadata,
               Column('id', Integer, primary_key=True),
               Column('user_id', Integer),
               Column('order_date', String))

# Step 3: Create the tables in the database
metadata.create_all(engine)

# Step 4: Insert sample data into the tables with explicit transaction commit
with engine.connect() as conn:
    # Inserting into 'users' table
    conn.execute(users.insert(), [
        {'id': 1, 'name': 'Alice', 'email': 'alice@email.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@email.com'}
    ])

    # Inserting into 'orders' table
    conn.execute(orders.insert(), [
        {'id': 1, 'user_id': 1, 'order_date': '2024-01-01'},
        {'id': 2, 'user_id': 2, 'order_date': '2024-02-01'}
    ])

    # Explicit commit (although with SQLAlchemy, this should generally happen automatically)
    conn.commit()

# Step 5: Query data from both tables (example: JOIN the tables without renaming columns)
query = """
SELECT users.id, users.name, users.email, orders.id as ord_id, orders.order_date
FROM users
JOIN orders ON users.id = orders.user_id
"""

# Step 6: Load the query result into a Pandas DataFrame
with engine.connect() as conn:
    df = pd.read_sql(query, conn)  # Execute query and load into DataFrame

# Step 7: Rename columns in the DataFrame
df = df.rename(columns={
    'id': 'User_ID',

})

# Display the result
print(df)