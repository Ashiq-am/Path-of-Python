import psycopg

with psycopg.connect("dbname=fla user=postgres password=root host=localhost") as conn:
    with conn.cursor() as cur:
        try:
            for i in range(0, 9, 1):
                with conn.transaction() as tx:
                    print(i)
                    cur.execute("INSERT INTO psy (num, data) VALUES (%s, %s)", (i, "data"))
                    if i > 5:
                        raise psycopg.Rollback
                    cur.execute("SELECT * from psy")
                    data = cur.fetchall()
                    print(data)
                conn.commit()

            print("up is in the try block")
        except psycopg.Rollback:
            conn.rollback()
        finally:
            cur.close()
            conn.close()

