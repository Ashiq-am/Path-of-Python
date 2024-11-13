# books with ratings greater than 3 published after 2000
pprint.pprint(list(books.find({'$and':
							[{"ratings":
								{'$gt':3}},
								{"publish":
								{'$gt':datetime.datetime(2000, 12, 31)
								}
								}
							]
							}
							)
				)
			)
