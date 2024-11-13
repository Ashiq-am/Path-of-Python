def parse_links(self, html):
    soup = BeautifulSoup(html, 'html.parser')
    Anchor_Tags = soup.find_all('a', href=True)

    for link in Anchor_Tags:
        url = link['href']

        if url.startswith('/') or url.startswith(self.root_url):
            url = urljoin(self.root_url, url)

            if url not in self.scraped_pages:
                self.crawl_queue.put(url)
