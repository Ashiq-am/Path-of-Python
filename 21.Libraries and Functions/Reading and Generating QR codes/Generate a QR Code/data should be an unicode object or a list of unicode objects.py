# use these for custom data formats eg. url, phone number, VCARD
# data should be an unicode object or a list of unicode objects
data_encode = {
	'text': lambda data: data,
	'url': encode_url,
	'email': lambda data: 'mailto:' + re.compile(
		r'^mailto:', re.IGNORECASE
	).sub('', data),
	'emailmessage': lambda data: 'MATMSG:TO:' + data[0] + ';SUB:' + data[1] +
						';BODY:' + data[2] + ';;',
	'telephone': lambda data: 'tel:' + re.compile(
		r'^tel:', re.IGNORECASE
	).sub('', data),
	'sms': lambda data: 'SMSTO:' + data[0] + ':' + data[1],
	'mms': lambda data: 'MMSTO:' + data[0] + ':' + data[1],
	'geo': lambda data: 'geo:' + data[0] + ', ' + data[1],
	'bookmark': lambda data: "MEBKM:TITLE:" + data[0] + ";URL:" +
									data[1] + ";;",
	# phonebook or meCard should be a list of tuples like this:
	# [('N', 'Name'), ('TEL', '231698890'), ...]
	'phonebook': lambda data: "MECARD:" + ";".join([":".join(i)
										for i in data]) + ";"
}












"""We can also add email data, sms data, mms data, bookmarks, etc to the QR code. 
The following code excerpt is taken from the source code, which specifies the various datatypes that can 
be used along with the format of the data that would be required for its usage"""













"""From the above code, we observe the various data types that can be assigned and used while creating QR codes. 
For example, to use a bookmark as data we must provide data as a list, consisting of a title and the url. 
To accomplish this, we must do the following"""





















# Python 2.x program to generate QR code
from qrtools import QR

# creates the QR object
my_QR = QR(data = [u"geeksforgeeks", u"https://www.geeksforgeeks.org/"],
									data_type = 'bookmark')

# encodes to a QR code
my_QR.encode()
