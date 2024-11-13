import datetime
import pytz

dtObject_utc = datetime.datetime.now(pytz.utc)

dtObject_asia = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
dtObject_usc = datetime.datetime.now(pytz.timezone('US/Central'))
dtObject_turkey = datetime.datetime.now(pytz.timezone('Turkey'))
dtObject_eoslo = datetime.datetime.now(pytz.timezone('Europe/Oslo'))
dtObject_abelem = datetime.datetime.now(pytz.timezone('America/Belem'))

print(dtObject_utc)

print(dtObject_asia)
print(dtObject_usc)
print(dtObject_turkey)
print(dtObject_eoslo)
print(dtObject_abelem)
