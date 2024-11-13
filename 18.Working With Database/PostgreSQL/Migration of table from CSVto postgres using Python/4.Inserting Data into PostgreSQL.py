query = '''
INSERT INTO employee(name, age, gender)
VALUES (%s, %s, %s);
'''

for _, row in data.iterrows():
    cursor.execute(query, tuple(row))

conn.commit()
