# imports
import sqlite3
from sqlite3 import Error
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_from_sheet():
    # name of the sheet
    # you should replace with the name
    # of your sheet
    sheet_name = "Details (Responses)"
    config = {Your_API

              # should contain the service account
              # key JSON as dict here
              }

    # use credentials to create a client to
    # interact with the Google Drive API
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    # credential object for authenticating
    creds_obj = ServiceAccountCredentials.from_json_keyfile_dict(config, scope)

    # initializing gspread client with the
    # credentials object
    client = gspread.authorize(creds_obj)

    # Find a workbook by name and open the
    # first sheet Make sure you use the
    # right name here.
    sheet = client.open(sheet_name).sheet1

    # returns all the data in the entire sheet
    return sheet.get_all_values()


class SQLite:
    # change this to your sqlite file path
    # if you keep then, then it will create
    # a sqlite database in your current working
    # directory
    DB_NAME = "db.sqlite"

    def __init__(self):
        self.conn = self.create_connection()
        self._get_or_create_table()

    @classmethod
    def create_connection(cls):
        """
        create a database connection to the SQLite database specified by db_name
        :return: Connection object or None
        """
        conn = None
        try:

            # connects or creates a sqlite3 file
            conn = sqlite3.connect(cls.DB_NAME)
            return conn
        except Error as e:
            print(e)

        # returns the connection object
        return conn

    def _get_or_create_table(self):
        """Creates the table if it does not exists"""

        # sql query to create a details table
        create_table_sql = """CREATE TABLE IF NOT EXISTS details (
			timestamp varchar(20) PRIMARY KEY,
			name varchar(30) NOT NULL,
			year varchar(3) NOT NULL
		)"""
        try:

            # initializing the query cursor
            c = self.conn.cursor()

            # executes the create table query
            c.execute(create_table_sql)
        except Error as e:

            # prints the exception if any errors
            # occurs during runtime
            print(e)

    def add_data_to_table(self, rows: list):
        """Inserts the data from sheets to the table"""

        # initializing sql cursor
        c = self.conn.cursor()

        # excluding the first row because it
        # contains the headers
        insert_table_sql = """INSERT INTO details (timestamp, name, year)
		VALUES (?, ?, ?);"""
        for row in rows[1:]:
            # inserts the data into the table
            # NOTE: the data needs to be in the order
            # which the values are provided into the
            # sql statement
            c.execute(insert_table_sql, tuple(row))

        # committing all the changes to the database
        self.conn.commit()

        # closing the connection to the database
        c.close()


if __name__ == '__main__':
    # fetches data from the sheets
    data = get_from_sheet()

    sqlite_util = SQLite()
    sqlite_util.add_data_to_table(data)
