from datetime import *
import pytz


tz_BANGALDESH = pytz.timezone('Asia/Dhaka')
datetime_BANGALDESH = datetime.now(tz_BANGALDESH)
print("BANGLADESH time:", datetime_BANGALDESH.strftime("%H:%M:%S"))
