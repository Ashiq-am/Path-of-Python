from itemadapter import ItemAdapter
import json


class ScrapytutorialPipeline:
    def process_item(self, item, spider):
        # calling dumps to create json data.
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def open_spider(self, spider):
        self.file = open('result.json', 'w')

    def close_spider(self, spider):
        self.file.close()
