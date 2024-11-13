import scrapy
import warnings
from scrapy.exceptions import ScrapyDeprecationWarning

def my_function():
	warnings.warn(
		"my_function() is deprecated, \
				use my_new_function() instead",
		ScrapyDeprecationWarning)
