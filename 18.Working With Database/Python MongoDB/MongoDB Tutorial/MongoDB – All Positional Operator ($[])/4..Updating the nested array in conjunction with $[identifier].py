""



"""

db.contributor.update({}, {$inc: {"marks.$[].firstsemester.$[newmarks]": 3}},
							{arrayFilters: [{newmarks: {$lte: 80}}], multi: true})


"""