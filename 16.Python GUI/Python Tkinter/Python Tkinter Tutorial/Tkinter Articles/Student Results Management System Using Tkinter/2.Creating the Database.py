con = sqlite3.connect('studentrecords.db')
c = con.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS StudentData(
                Name TEXT,
                Roll NUMBER,
                Gender TEXT,
                Maths NUMBER,
                Physics NUMBER,
                Chemistry NUMBER)""")
con.commit()
con.close()
