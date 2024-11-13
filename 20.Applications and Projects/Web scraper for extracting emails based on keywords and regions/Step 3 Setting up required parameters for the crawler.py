# create class to extract email ids
class email_extractor(CrawlSpider):
    # adjusting parameters
    name = 'email_ex'

    def __init__(self, *args, **kwargs):
        super(email_extractor, self).__init__(*args, **kwargs)
        self.email_list = []
        self.query = " 'market places'.gmail.com "
