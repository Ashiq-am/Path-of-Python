# importing the module
import ipaddress

# converting IPv4 address to int
addr1 = ipaddress.ip_address('191.255.254.40')
addr2 = ipaddress.ip_address('0.0.0.123')
print(int(addr1))
print(int(addr2))

# converting IPv6 address to int
addr3 = ipaddress.ip_address('2001:db7:dc75:365:220a:7c84:d796:6401')
print(int(addr3))
