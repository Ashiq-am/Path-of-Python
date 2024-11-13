from itemadapter import ItemAdapter
import json # Json package of python module.


class ScrapytutorialPipeline:
	def process_item(self, item, spider): # default method
		# calling dumps to create json data.
		line = json.dumps(dict(item)) + "\n"
		# converting item to dict above, since dumps only intakes dict.
		self.file.write(line)				 # writing content in output file.
		return item

	def open_spider(self, spider):
		self.file = open('result.json', 'w')

	def close_spider(self, spider):
		self.file.close()
