from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import pandas as pd

# Step 1: Set up SQLAlchemy engine for an in-memory SQLite database
engine = create_engine('sqlite:///:memory:')  # In-memory SQLite database

# Step 2: Define the schema (metadata) for the tables
metadata = MetaData()

# Define the 'employees' table
employees = Table('employees', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('department', String))

# Define the 'projects' table
projects = Table('projects', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('employee_id', Integer),
                 Column('project_name', String),
                 Column('budget', Integer))

# Step 3: Create the tables in the database
metadata.create_all(engine)

# Step 4: Insert sample data into the tables
with engine.connect() as conn:
    conn.execute(employees.insert(), [
        {'id': 1, 'name': 'Sophia', 'department': 'Engineering'},
        {'id': 2, 'name': 'Liam', 'department': 'Marketing'}
    ])
    conn.execute(projects.insert(), [
        {'id': 1, 'employee_id': 1, 'project_name': 'Project A', 'budget': 100000},
        {'id': 2, 'employee_id': 2, 'project_name': 'Project B', 'budget': 150000}
    ])
    conn.commit()

# Step 5: Query data from both tables
query = """
SELECT employees.id, employees.name, employees.department,
       projects.id AS project_id, projects.project_name, projects.budget
FROM employees
JOIN projects ON employees.id = projects.employee_id
"""

# Step 6: Load the query result into a Pandas DataFrame
with engine.connect() as conn:
    df = pd.read_sql(query, conn)

# Step 7: Display the columns before renaming
print("Columns before renaming:")
print(df.columns)

# Step 8: Rename columns in the DataFrame using rename() based on actual column names
df = df.rename(columns={
    'id': 'employee_id',  # Rename the first 'id' from employees
    'project_id': 'project_id',  # 'project_id' already has the correct name
    'name': 'employee_name',  # Rename 'name' from employees to 'employee_name'
    'department': 'employee_department',  # Rename 'department' from employees
    'project_name': 'project_name',  # Rename 'project_name' (no change needed)
    'budget': 'project_budget'  # Rename 'budget' from projects
})

# Step 9: Display the final DataFrame
print("\nQuery with renaming columns in DataFrame using rename():")
print(df)