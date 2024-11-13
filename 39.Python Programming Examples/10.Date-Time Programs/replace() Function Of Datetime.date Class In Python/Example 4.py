from datetime import datetime

Date = datetime(2010, 2, 12, 8, 50, 23)
print("Original date and time : ", Date)

New_date = Date.replace(hour=1,
						minute=3,
						second=12)
print("After modify date and time : ", New_date)
