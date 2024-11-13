def getting_interface(ipaddress):
	for interface in ifaces.values():
		if interface.ip == ipaddress:
			return {"name":interface.name,"mac":interface.mac}
