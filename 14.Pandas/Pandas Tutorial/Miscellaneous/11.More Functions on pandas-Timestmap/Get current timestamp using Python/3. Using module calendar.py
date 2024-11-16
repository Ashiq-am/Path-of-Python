# using calendar module
# using time module
import calendar
import time

# gmt stores current gmtime
gmt = time.gmtime()
print("gmt:-", gmt)

# ts stores timestamp
ts = calendar.timegm(gmt)
print("timestamp:-", ts)
