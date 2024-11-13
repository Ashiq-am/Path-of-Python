def getting_ip_of_access_point():
	return scapy.conf.route.route("8.8.8.8")[2]
