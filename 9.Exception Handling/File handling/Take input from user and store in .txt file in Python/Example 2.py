temp = input("Please enter your information!! ")
try:
	with open('gfg.txt', 'w') as gfg:
		gfg.write(temp)
except Exception as e:
	print("There is a Problem", str(e))
