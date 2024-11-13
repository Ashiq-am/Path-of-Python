# importing modules
import whois
import sys

# Use exception handle program
# and get information from whois
try:
    domain = whois.whois("geeksforgeeks.com")
    if domain.domain_name == None:
        sys.exit(1)

except:
    print("This domain is available")
else:
    print("Oops! this domain already purchased")
