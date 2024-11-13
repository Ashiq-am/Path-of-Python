# Import libraries
import dns.resolver

# Finding PTR record
result = dns.resolver.query('116.62.218.34.in-addr.arpa', 'PTR')

# Printing record
for val in result:
	print('PTR Record : ', val.to_text())
