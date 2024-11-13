def calculate_time(start, stop):

	# to calculate unavailability time
	difference = stop - start
	seconds = float(str(difference.total_seconds()))
	return str(datetime.timedelta(seconds=seconds)).split(".")[0]
