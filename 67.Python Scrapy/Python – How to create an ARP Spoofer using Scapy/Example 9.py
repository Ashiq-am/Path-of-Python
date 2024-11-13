def restore(destination_ip, source_ip):
	destination_mac = get_mac(destination_ip)
	source_mac = get_mac(source_ip)
	packet = scapy.ARP(op = 2, pdst = destination_ip,
							hwdst = destination_mac,
				psrc = source_ip, hwsrc = source_mac)

	scapy.send(packet, verbose = False)
