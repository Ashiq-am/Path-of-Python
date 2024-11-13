query = '''
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10)
);
'''

cursor.execute(query)
conn.commit()
