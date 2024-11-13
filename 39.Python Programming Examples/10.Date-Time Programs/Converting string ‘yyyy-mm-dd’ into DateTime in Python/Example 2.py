# import the datetime module
import datetime

# datetime in string format for list of dates
input = ['2021/05/25', '2020/05/25', '2019/02/15', '1999/02/4']

# format
format = '%Y/%m/%d'
for i in input:
    # convert from string format to datetime format
    # and get the date
    print(datetime.datetime.strptime(i, format).date())
