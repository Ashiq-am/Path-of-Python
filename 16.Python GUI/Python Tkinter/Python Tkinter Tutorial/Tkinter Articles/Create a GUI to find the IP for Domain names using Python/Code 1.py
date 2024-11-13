# import module
from iplookup import iplookup

#create object of iplookup
ip = iplookup.iplookup

# Input by geek
# domain name
domain = "facebook.com"

# pass the domain
# into iplookup obj
result = ip(domain)

# traverse the ip
print("Domain name : ",domain)
print("Ip : ",result)
