# slower
from urllib3.connectionpool import xrange

x = [i for i in range(0,10,2)]
print(x)

# faster
x = [i for i in xrange(0,10,2)]
print(x)
