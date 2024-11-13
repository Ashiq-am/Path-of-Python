from databases import Database
import asyncio


async def insert_records():
    database = Database('postgresql://username:passowrd@host:5432/database')
    try:
        await database.connect()
        print('Connected to Database')

        # Insert into table.
        query = """INSERT INTO GfgExample(id,name) VALUES (:id ,:name)"""
        values = [
            {"id": 1, "name": "abc"},
            {"id": 2, "name": "xyz"}
        ]
        await database.execute_many(query=query, values=values)
        print('Inserted values in GfgExample Table Successfully')

        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')


if __name__ == '__main__':
    asyncio.run(insert_records())
