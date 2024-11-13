rules = (
	Rule(LinkExtractor(allow=r'utils/'),
		callback='parse_item', follow = True),
)
