# importing datetime and timedelta from
# datetime module
from datetime import datetime, timedelta


# function to return time
def get_time(current_time):
    # creating timedelta object with negative
    # values
    time_obj = timedelta(hours=15, minutes=25)

    # getting required time
    req_time = current_time - time_obj

    # splitting time from resultant datetime
    time = req_time.time()

    # returning time
    return time


# main function
if __name__ == '__main__':
    # getting current date and time
    current_datetime = datetime.now()

    # calling function to get the time
    resulted_time = get_time(current_datetime)

    # printng current time
    print(f'Current time is: {current_datetime.time()}')

    # printng resultant time after using timedelta
    print(f'Resultant time after using timedelta object is: {resulted_time}')
