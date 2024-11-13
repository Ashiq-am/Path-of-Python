# import datetime module
import datetime

# convert datetime to epoch using timestamp()
# from time stamp 2021/7/7/0/0/0
epoch = datetime.datetime(2021, 7, 7, 0, 0, 0).timestamp()
print(epoch)


# convert datetime to epoch using timestamp()
# from time stamp 2021/3/3/4/3/4
epoch = datetime.datetime(2021, 3, 3, 4, 3, 4).timestamp()
print(epoch)

# convert datetime to epoch using timestamp()
# from time stamp 2021/7/7/12/12/34
epoch = datetime.datetime(2021, 7, 7, 12, 12, 34).timestamp()
print(epoch)

# convert datetime to epoch using timestamp()
# from time stamp 2021/7/7/12/56/00
epoch = datetime.datetime(2021, 7, 7, 12, 56, 00).timestamp()
print(epoch)
