to = ["klm@gmail.com", "xyz@gmail.com", "abc@gmail.com"]
smtp.sendmail(from_addr="Your Login Email",
			to_addrs=to, msg=msg.as_string())
smtp.quit()
