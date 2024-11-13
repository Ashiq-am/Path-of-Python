from databases import Database
import asyncio


async def create_table():
    database = Database('postgresql://username:password@host:5432/database')
    try:
        await database.connect()
        print('Connected to Database')

        # Create a table.
        query = """CREATE TABLE GfgExample (id INTEGER PRIMARY KEY, name VARCHAR(100))"""
        print('Created Table GfgExample Successfully')
        await database.execute(query=query)

        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')


if __name__ == '__main__':
    asyncio.run(create_table())
