# import necessary packages
from sqlalchemy import func

# pass the sql query statement to
# the execute function
result = engine.execute('SELECT div(book_price,3)\
AS minimum FROM books')

# use fetchall() to return all result
result.fetchall()
