# Import libraries
import dns.resolver

# Finding TXT record
result = dns.resolver.query('geeksforgeeks.org', 'TXT')

# Printing record
for val in result:
	print('TXT Record : ', val.to_text())
