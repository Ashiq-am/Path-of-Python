import os
import datetime as dt

print("Before conversion :")

# returns seconds since epoch
print("last access time :",os.path.getatime(os.getcwd()))
print("last modification time :",os.path.getmtime(os.getcwd()))

print("After conversion :")

# formatting the return value
access_time=dt.datetime.fromtimestamp(os.path.getatime(os.getcwd())).strftime('%Y-%m-%d %I:%M %p')
modification_time=dt.datetime.fromtimestamp(os.path.getmtime(os.getcwd())).strftime('%Y-%m-%d %I:%M %p')

print("last access time :",access_time)
print("last modification time :",modification_time)
