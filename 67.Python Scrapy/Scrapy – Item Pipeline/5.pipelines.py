from itemadapter import ItemAdapter
import sqlite3


class ScrapytutorialPipeline(object):

    # init method to initialize the database
    # and create connection and tables
    def __init__(self):
        self.create_conn()
        self.create_table()

    # create connection method to create
    # database or use database to store scraped data
    def create_conn(self):
        self.conn = sqlite3.connect("mydata.db")
        self.curr = self.conn.cursor()

    # Create table method
    # using SQL commands to create table
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS firsttable""")
        self.curr.execute("""create table firsttable(
						Quote text
						)""")

    # store items to databases.
    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        self.curr.execute("""insert into firsttable values (?)""", (
            item['Quote'][0],  # extracting item.
        ))
        self.conn.commit()
