def getting_ip_of_this_device():
	return scapy.conf.route.route("8.8.8.8")[1]
