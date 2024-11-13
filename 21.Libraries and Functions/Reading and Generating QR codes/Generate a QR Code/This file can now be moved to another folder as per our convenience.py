# Python 2.x program to generate QR code
from qrtools import QR

import os
my_QR = QR(data = u"Example")
my_QR.encode()

# command to move the QR code to the desktop
os.system("sudo mv " + my_QR.filename + " ~/Desktop")













'''The pixel value of the QR code may also be changed by specifying the value during the creation of the QR object. 
The default size tends to be a little small for reading using scanners on smartphones, 
so a size of around 10 would be ideal for such purposes, for example:



my_QR = QR(data = u"example", pixel_size = 10)




'''