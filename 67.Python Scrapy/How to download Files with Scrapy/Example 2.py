rules = (
	Rule(LinkExtractor(allow = r'Items/'),
		callback = 'parse_item',
		follow = True),
)
