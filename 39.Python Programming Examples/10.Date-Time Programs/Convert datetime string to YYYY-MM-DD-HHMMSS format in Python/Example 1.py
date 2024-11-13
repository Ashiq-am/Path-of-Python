# import datetime module
from datetime import datetime

# consider date in string format
my_date = "30-May-2020-15:59:02"

# convert datetime string into date,month,day and
# hours:minutes:and seconds format using strptime
d = datetime.strptime(my_date, "%d-%b-%Y-%H:%M:%S")

# convert datetime format into %Y-%m-%d-%H:%M:%S
# format using strftime
print(d.strftime("%Y-%m-%d-%H:%M:%S"))
