from unicodedata import normalize

print ('%r' % normalize('NFD', u'\u00C7'))
print ('%r' % normalize('NFC', u'C\u0327'))
print ('%r' % normalize('NFKD', u'\u2460'))
