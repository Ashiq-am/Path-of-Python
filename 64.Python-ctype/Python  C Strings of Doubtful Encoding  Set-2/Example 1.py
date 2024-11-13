raw = b'Spicy Jalape\xc3\xb1o\xae'

print (raw.decode('utf-8', 'ignore'))

print (raw.decode('utf-8', 'replace'))
