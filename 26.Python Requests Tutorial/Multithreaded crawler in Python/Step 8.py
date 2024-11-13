def post_scrape_callback(self, res):
    result = res.result()

    if result and result.status_code == 200:
        self.parse_links(result.text)
        self.scrape_info(result.text)
