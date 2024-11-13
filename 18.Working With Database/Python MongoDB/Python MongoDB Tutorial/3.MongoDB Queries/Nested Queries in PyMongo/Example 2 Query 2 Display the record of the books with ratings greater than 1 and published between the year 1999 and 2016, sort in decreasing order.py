# between 1999-2016
query ={'$and':
		[{"publish":
		{'$gte':datetime.datetime(1999, 1, 1)}},
		{"publish":
		{'$lte':datetime.datetime(2016, 12, 31)}}]}

# books with ratings greater than 1
# and published between the year
# 1999-2016, sort in decreasing order.
pprint.pprint(list(books.find({'$and':
							[{"ratings":
								{'$gt':1}},
								query]}).sort("publish", -1)))
