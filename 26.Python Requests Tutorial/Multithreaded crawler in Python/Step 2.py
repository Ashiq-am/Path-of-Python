if __name__ == '__main__':
	cc = MultiThreadedCrawler("https://www.geeksforgeeks.org/")
	cc.run_web_crawler()
	cc.info()
