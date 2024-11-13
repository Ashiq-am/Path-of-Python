# MANIPULATING DATETIME
from datetime import date, timedelta

current_date = date.today()

print("CURRENT DAY : ",current_date)

print("OLD Date : ",current_date - timedelta(17))
