# Import libraries
import dns.resolver

# Finding CNAME record
result = dns.resolver.query('geeksforgeeks.org', 'CNAME')

# Printing record
for val in result:
	print('CNAME Record : ', val.target)
