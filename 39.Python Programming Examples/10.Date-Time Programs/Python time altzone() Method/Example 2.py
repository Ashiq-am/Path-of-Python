# import time module
import time


# get_zone function to get the
# current time between current time zone and UTC
# by using timezone and altzone method
def get_zone():
    dst = time.daylight and time.localtime().tm_isdst

    # get altzone if there exists dst otherwise
    # get timezone
    offset = time.altzone if dst else time.timezone

    # check if offset greater than 0
    westerly = offset > 0

    # get the minutes and seconds
    minutes, seconds = divmod(abs(offset), 60)
    hours, minutes = divmod(minutes, 60)

    # return the timezone
    return '{}{:02d}{:02d}'.format('-' if westerly else '+', hours, minutes)


# call the function
get_zone()
