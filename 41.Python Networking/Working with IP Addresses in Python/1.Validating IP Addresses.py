# Import module
import ipaddress

# Example of valid IPv4 address
print (ipaddress.ip_address(u'175.198.42.211'))

# Invalid IPv4 address raises error
print (ipaddress.ip_address(u'175.198.42.270'))
