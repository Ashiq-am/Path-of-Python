import pyspeedtest


test = pyspeedtest.SpeedTest("www.youtube.com")

test.ping()
test.download()
test.upload()
