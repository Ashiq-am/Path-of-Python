# importing datetime and timedelta from datetime module
from datetime import datetime, timedelta


# function to return time
def get_datetime(current_datetime):
    # creating timedelta object with negative values
    time_obj = timedelta(weeks=-1, days=-4,
                         hours=-15, minutes=-25,
                         seconds=-54)

    # getting required time and time
    req_time = current_datetime + time_obj

    # returning date and time
    return req_time


# main function
if __name__ == '__main__':
    # getting current date and time
    current_datetime = datetime.now()

    # calling function to get the date and time
    resulted_time = get_datetime(current_datetime)

    # printng current date and time
    print(f'Current time is: {current_datetime}')

    # printng resultant date and time after using timedelta
    print(f'Resultant time after using timedelta object is: {resulted_time}')
