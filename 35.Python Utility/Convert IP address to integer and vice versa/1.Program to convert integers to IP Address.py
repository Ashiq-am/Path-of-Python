# importing the module
import ipaddress

# converting int to IPv4 address
print(ipaddress.ip_address(3221225000))
print(ipaddress.ip_address(123))

# converting int to IPv6 address
print(ipaddress.ip_address(42540766400282592856903984001653826561))
