class MultiThreadedCrawler:

	def __init__(self, seed_url):
		self.seed_url = seed_url
		self.root_url = '{}://{}'.format(urlparse(self.seed_url).scheme,
										urlparse(self.seed_url).netloc)
		self.pool = ThreadPoolExecutor(max_workers=5)
		self.scraped_pages = set([])
		self.crawl_queue = Queue()
		self.crawl_queue.put(self.seed_url)
