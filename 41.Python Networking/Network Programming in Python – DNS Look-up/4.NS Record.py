# Import libraries
import dns.resolver

# Finding NS record
result = dns.resolver.query('geeksforgeeks.org', 'NS')

# Printing record
for val in result:
	print('NS Record : ', val.to_text())
