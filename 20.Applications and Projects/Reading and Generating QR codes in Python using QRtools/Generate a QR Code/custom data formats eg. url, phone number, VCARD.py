# use these for custom data formats eg. url, phone number, VCARD
# data should be an unicode object or a list of unicode objects
data_encode = {
	'text': lambda data: data,
	'url': encode_url,
	'email': lambda data: 'mailto:' + re.compile(r'^mailto:', re.IGNORECASE).sub('', data),
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
