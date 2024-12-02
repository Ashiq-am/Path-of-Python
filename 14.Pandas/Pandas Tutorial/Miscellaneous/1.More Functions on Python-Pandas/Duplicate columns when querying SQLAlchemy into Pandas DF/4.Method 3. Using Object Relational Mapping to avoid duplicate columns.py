from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

# --- Step 1: Define Database and Tables ---
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total = Column(Integer)

# --- Step 2: Connect to Database ---
engine = create_engine("sqlite:///example.db", echo=True)
Base.metadata.create_all(engine)  # Creates tables if not already present

# --- Step 3: Insert Sample Data (if necessary) ---
def insert_sample_data():
    # Use session to handle transactions
    session = Session()
    session.add_all([
        User(id=1, name='Alice'),
        User(id=2, name='Bob'),
        User(id=3, name='Charlie'),
        Order(id=101, user_id=1, total=200),
        Order(id=102, user_id=2, total=150),
        Order(id=103, user_id=3, total=300)
    ])
    session.commit()  # Commit all changes in one go
    session.close()

# Uncomment below line to insert data only once
insert_sample_data()

# --- Step 4: Create a Session ---
Session = sessionmaker(bind=engine)
session = Session()

# --- Step 5: Query Specific Columns ---
query = session.query(
    User.id.label("user_id"),
    Order.id.label("order_id"),
    Order.total.label("order_total")
).filter(User.id == Order.user_id)

# --- Step 6: Load Query Results into a Pandas DataFrame ---
df = pd.read_sql(query.statement, session.bind)

# --- Step 7: Print the DataFrame ---
print(df)

# --- Step 8: Close the Session ---
session.close()