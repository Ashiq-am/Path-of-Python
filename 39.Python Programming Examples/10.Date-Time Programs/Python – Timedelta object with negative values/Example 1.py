# importing datetime and timedelta from
# datetime module
from datetime import datetime, timedelta


# function to return date
def get_date(current_date):
    # creating timedelta object with negative
    # values
    date_obj = timedelta(days=-534)

    # getting required date
    req_date = current_date + date_obj

    # splitting date from resultant datetime
    date = req_date.date()

    # returning date
    return date


# main function
if __name__ == '__main__':
    # getting current date and time
    current_datetime = datetime.now()

    # calling function to get the date
    resulted_date = get_date(current_datetime)

    # printng current date
    print('Current date is:', current_datetime.date())

    # printng resultant date after using timedelta
    print('Resultant time after using timedelta object is:',
          resulted_date)
