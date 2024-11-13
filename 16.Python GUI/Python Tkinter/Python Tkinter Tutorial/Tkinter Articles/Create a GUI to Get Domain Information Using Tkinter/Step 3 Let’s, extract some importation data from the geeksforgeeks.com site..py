import whois

domain = whois.whois('geeksforgeeks.com')
print("Expration Date :",domain.expiration_date)
print("Email :", domain.emails)
print("Server name : ",domain.name_servers)
