try:
	response = requests.get(url)
except:
	engine.say("can, t access link, plz check you internet ")

news = json.loads(response.text)
for new in news['articles']:
	print("##############################################################\n")
	print(str(new['title']), "\n\n")
	engine.say(str(new['title']))
	print('______________________________________________________\n')

	engine.runAndWait()

	print(str(new['description']), "\n\n")
	engine.say(str(new['description']))
	engine.runAndWait()
	print("..............................................................")
	time.sleep(2)
