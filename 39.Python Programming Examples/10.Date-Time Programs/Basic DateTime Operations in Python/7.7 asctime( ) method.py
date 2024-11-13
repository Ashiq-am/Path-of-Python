import time
# method returns 24-character string of
# the following form − 'Mon March 15 23:21:05 2021'

local_time = time.localtime()
print ("asctime : ",time.asctime(local_time))
