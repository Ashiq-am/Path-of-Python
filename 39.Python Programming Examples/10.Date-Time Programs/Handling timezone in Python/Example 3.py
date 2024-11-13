import datetime
import pytz

# getting our local timezone
dtObject_local = datetime.datetime.now()

# converting local timezone to 'US/Central'
dtObject_usc = dtObject_local.astimezone(pytz.timezone('US/Central'))

# now converting 'US/Central' timezone to 'Pacific/Chuuk'
dtObject_pchuuk = dtObject_usc.astimezone(pytz.timezone('Pacific/Chuuk'))

print(dtObject_local)
print(dtObject_usc)
print(dtObject_pchuuk)
