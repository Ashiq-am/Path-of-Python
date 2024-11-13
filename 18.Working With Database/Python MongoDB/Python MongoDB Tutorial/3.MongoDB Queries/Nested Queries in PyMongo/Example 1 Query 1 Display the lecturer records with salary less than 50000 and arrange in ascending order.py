# lecturer records with salary less
# than 50000 and arrange in ascending order.
pprint.pprint(list(lecturers.find({"salary":
								{'$lt':50000}}).sort('salary', 1)))
