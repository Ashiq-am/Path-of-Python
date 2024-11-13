# Import libraries
import dns.resolver

# Finding AAAA record
result = dns.resolver.query('geeksforgeeks.org', 'AAAA')

# Printing record
for val in result:
	print('AAAA Record : ', ipval.to_text())
