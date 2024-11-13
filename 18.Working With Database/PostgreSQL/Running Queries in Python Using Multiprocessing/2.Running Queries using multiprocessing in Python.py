from multiprocessing.connection import Connection
import time, os
from multiprocessing import Pool, freeze_support
import psycopg2


def run():
    try:
        conn = psycopg2.connect(database="root", user='root',
                                password='root', host='127.0.0.1',
                                port='5432')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM root''')
        records = cursor.fetchall()
        return records
    except:
        print("Connection not established to the database")
        return -1


if __name__ == "__main__":

    freeze_support()
    print("Enter the number of times to run the above query")
    n = int(input())
    results = []

    with Pool(processes=os.cpu_count() - 1) as pool:

        for _ in range(n):
            res = pool.apply_async(run)
            results.append(res)
            res = [result.get() for result in results]

    print(res)
    pool.close()
    pool.join()
