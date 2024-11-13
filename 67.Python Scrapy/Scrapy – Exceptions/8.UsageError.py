import scrapy
from scrapy.exceptions import UsageError


def my_script(args):

	if not args.input_file:
		raise UsageError("Input file is required")
