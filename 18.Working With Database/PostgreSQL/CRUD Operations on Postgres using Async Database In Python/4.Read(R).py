from databases import Database
import asyncio


async def find_records():
    database = Database('postgresql://username:password@host:5432/database')
    try:
        await database.connect()
        print('Connected to Database')

        # Select all records from table.
        query = """SELECT * FROM GfgExample"""
        rows = await database.fetch_all(query=query)
        print('Read the values in GfgExample Table Successfully')
        print('Printing Id Values Fetched from GfgExample Table')
        print(rows[0]['id'])
        print(rows[1]['id'])

        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')


if __name__ == '__main__':
    asyncio.run(find_records())
