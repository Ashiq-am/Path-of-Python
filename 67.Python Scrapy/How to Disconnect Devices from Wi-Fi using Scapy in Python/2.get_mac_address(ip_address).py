def get_mac_address(ip_address):
	arp_request = ARP(pdst=ip_address)
	arp_response = sr1(arp_request,
					timeout=1, verbose=False)
	if arp_response is not None:
		return arp_response.hwsrc
	else:
		return None
