import psycopg
import psycopg2

##isolation_level = psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE

with psycopg.connect("dbname=fla user=postgres password=root host=localhost") as conn:
    with conn.cursor() as cur:
        conn._read_only = True
        cur.execute("INSERT INTO psy (num, data) VALUES (%s, %s)", (9999, "data"))
        conn.commit()

        print("up is in the try block")

