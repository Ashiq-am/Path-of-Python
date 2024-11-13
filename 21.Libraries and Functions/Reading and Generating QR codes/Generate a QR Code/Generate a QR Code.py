# Python 2.x program to generate QR code
import qrtools
import QR

# creates the QR object
my_QR = QR(data = u"Example")

# encodes to a QR code
my_QR.encode()











'''If the program runs successfully, it returns a value of 0, and the QR code is stored in the tmp folder. 
To know the exact location, use the following command


print my_QR.filename


'''
