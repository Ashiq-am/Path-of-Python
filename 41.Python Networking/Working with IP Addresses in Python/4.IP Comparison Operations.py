# Import module
import ipaddress

# Comparison
print(ipaddress.IPv4Address(u'175.199.42.211') >
	ipaddress.IPv4Address(u'175.198.42.255'))

print(ipaddress.IPv6Address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334')
	== ipaddress.IPv6Address(u'2001:0dff:85a3:2bfe:070d:8a2e:0370:7334'))

print(ipaddress.IPv4Address(u'179.198.42.211') !=
	ipaddress.IPv4Address(u'175.198.42.255'))

print(ipaddress.IPv6Address(u'2001:0db8:85a3:2bfe:070d:8a2e:0370:7334') <
	ipaddress.IPv6Address(u'2001:0dff:85a3:2bfe:070d:8a2e:0370:7334'))
