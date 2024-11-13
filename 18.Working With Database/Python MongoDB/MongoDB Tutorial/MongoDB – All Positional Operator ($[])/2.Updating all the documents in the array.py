''


"""

db.contributor.update({}, {$inc: {"articles.$[].tArticles": -10}},
						{multi: true})


"""