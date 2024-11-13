''


"""

db.contributor.update({points: {$ne: 25}},
					{$inc: {"points.$[]": 20}},
						{multi: true})


"""