import schedule
import time
from scrapy import cmdline

def crawl():
	cmdline.execute("scrapy crawl my_spider".split())
