from datetime import datetime

# Using strptime() with milliseconds

date_time = datetime.strptime(
	"17 Oct 2021 15:48:35.525001", "%d %b %Y %H:%M:%S.%f")

print(date_time)
