from itertools import cycle

import requests

proxies = to_get_proxies()

# to rotate through the list of IPs
proxyPool = cycle(proxies)

# insert the url of the website you want to scrape.
url = ''

for i in range(1, 11):

    # Get a proxy from the pool
    proxy = next(proxyPool)
    print("Request #%d" % i)

    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        print(response.json())

    except:

        # One has to try the entire process as most
        # free proxies will get connection errors
        # We will just skip retries.
        print("Skipping. Connection error")
