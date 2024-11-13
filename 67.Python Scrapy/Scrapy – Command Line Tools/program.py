from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    # requires the use of project
    requires_project = True

    # syntax for command
    def syntax(self):
        return '[options]'

    # description of command
    def short_desc(self):
        return 'Runs the spider using custom command'

    # the main running command
    def run(self, args, opts):
        # derieves to spider of scrapy project
        spider = self.crawler_process.spiders.list()

        # calls crawl command for that particular spider
        self.crawler_process.crawl(spider[0], **opts.__dict__)

        # starts the crawl
        self.crawler_process.start()
