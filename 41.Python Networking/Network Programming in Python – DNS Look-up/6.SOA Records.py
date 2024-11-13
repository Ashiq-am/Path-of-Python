# Import libraries
import dns.resolver

# Finding SOA record
result = dns.resolver.query('geeksforgeeks.org', 'SOA')

# Printing record
for val in result:
	print('SOA Record : ', val.to_text())
