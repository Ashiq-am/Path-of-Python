import datetime
import pytz

naive_dt = datetime.datetime(2022, 1, 1, 12, 0, 0)
aware_dt = pytz.timezone('America/New_York').localize(naive_dt)

print(naive_dt)
print(aware_dt)
