from threading import Semaphore
import urllib.request

# five threads are allowed to run at once (at max)
_fetch_url_sema = Semaphore(5)

def fetch_url(url):
	with _fetch_url_sema:
		return urllib.request.urlopen(url)
