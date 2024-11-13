def run_web_crawler(self):
    while True:
        try:
            print("\n Name of the current executing process: ",
                  multiprocessing.current_process().name, '\n')
            target_url = self.crawl_queue.get(timeout=60)

            if target_url not in self.scraped_pages:
                print("Scraping URL: {}".format(target_url))
                self.scraped_pages.add(target_url)
                job = self.pool.submit(self.scrape_page, target_url)
                job.add_done_callback(self.post_scrape_callback)

        except Empty:
            return
        except Exception as e:
            print(e)
            continue
