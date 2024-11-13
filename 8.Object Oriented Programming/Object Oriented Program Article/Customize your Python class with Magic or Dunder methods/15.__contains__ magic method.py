import datetime

class DateClass(object):
	def __init__(self, startDate, endDate):
		self.startDate = startDate
		self.endDate = endDate

	def __contains__(self, item):
		""" check whether a date is between the given range and
		return true or false"""
		return self.startDate <= item <= self.endDate

dtObj = DateClass(datetime.date(2019, 1, 1), datetime.date(2021, 12, 31))
result = datetime.date(2020, 6, 4) in dtObj
print("Whether (2020, 6, 4) is within the mentioned date range? ", result)

result = datetime.date(2022, 8, 2) in dtObj
print("Whether (2022, 8, 2) is within the mentioned date range? ", result)
