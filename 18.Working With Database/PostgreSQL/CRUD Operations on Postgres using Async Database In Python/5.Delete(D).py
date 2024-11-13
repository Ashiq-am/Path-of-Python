from databases import Database
import asyncio


async def delete_table():
    database = Database('postgresql://username:password@host:5432/database')
    try:
        await database.connect()
        print('Connected to Database')

        # Delete from table.
        query = """Delete from GfgExample"""
        await database.execute(query=query)
        print('Deleted All Records For GfgExample Successfully')

        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')


if __name__ == '__main__':
    asyncio.run(delete_table())
