# booklist\items.py

# Define here the models for your scraped items
from scrapy.item import Item, Field

class BooklistItem(Item):
	url = Field()
	title = Field()
	price = Field()
