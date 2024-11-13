# code
import time

# method mktime() is the inverse function of localtime()
# Its argument is the struct_time or full 9-tuple and
# it returns a floating point number, for compatibility with time().

t = (2016, 2, 15, 10, 13, 38, 1, 48, 0)
d = time.mktime(t)
print ("time.mktime(t) : %f" % d)
print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(d)))
