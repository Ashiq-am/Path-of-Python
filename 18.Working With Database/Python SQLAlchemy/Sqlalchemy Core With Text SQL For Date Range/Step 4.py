from sqlalchemy import text
sql_query = text("SELECT * FROM mytable WHERE date_column >= :start_date AND date_column <= :end_date")
