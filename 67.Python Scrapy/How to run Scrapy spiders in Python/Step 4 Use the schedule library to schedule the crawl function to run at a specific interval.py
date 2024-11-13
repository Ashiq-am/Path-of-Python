schedule.every(5).minutes.do(crawl)

while True:
	schedule.run_pending()
	time.sleep(1)
