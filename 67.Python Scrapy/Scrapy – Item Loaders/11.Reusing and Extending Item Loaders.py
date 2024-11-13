# Import the MapCompose built-in processor
from itemloaders.processors import MapCompose

# Import the existing BookLoader
# Item loader used for scraping book data
from myproject.ItemLoaders import BookLoader

# Custom function to remove the '*'
def strip_asterisk(x):
	return x.strip('*')

# Extend and reuse the existing BookLoader class
class SiteSpecificLoader(BookLoader):
	authorname = MapCompose(strip_asterisk,
							BookLoader.authorname)
