# lecturer records with salary greater than 40000
# in department_id 1 and sort according to their
# salary in descending order.
pprint.pprint(list(lecturers.find({'$and':
								[{"d_id":1},
									{"salary":
									{'$gte':50000}}]}).sort("salary", -1)))
