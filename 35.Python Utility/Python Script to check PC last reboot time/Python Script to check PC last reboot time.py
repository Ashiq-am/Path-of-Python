import psutil
import datetime

# returns the time in seconds since the epoch
last_reboot = psutil.boot_time()

# coverting the date and time in readable format
print(datetime.datetime.fromtimestamp(last_reboot))
