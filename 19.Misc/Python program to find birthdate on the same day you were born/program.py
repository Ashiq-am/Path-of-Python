import datetime
import calendar

weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


# get_birth day
def split_date(birthday):
    # Split it to year, month and day
    year, month, day = birthday.split('-')
    return year, month, day


def get_birthday(birthday):
    year, month, day = split_date(birthday)

    # Get a date object for the day of birth
    bdate = datetime.datetime(int(year), int(month), int(day))

    # Get the integer weekday for the day of birth
    weekday = bdate.weekday()

    # Tell the user
    day = weekdays[weekday]

    return day


def listToString(x):
    # initialize an empty string
    String = " "

    # return string
    return (String.join(x))


def true_birthdays(birthdate):
    year, month, day = split_date(birthdate)

    # get the year from birthday
    year = birthdate[:4].split('-')

    # convert list to string
    year = listToString(year)

    # get the weekday you are born
    d_day = get_birthday(birthdate)

    # list of true birthdate[birthday that have same
    # weekday as the day you were born]
    true_BD = []

    j = 0

    for i in range(int(year), 2050):

        # add + j to birth year
        new_year = int(year) + j

        # construct new birthday
        new_birthday = str(str(new_year) + "-" + month + "-" + day)

        # get weekday of the new birthday
        new_d_day = get_birthday(new_birthday)

        # if birthday that have same weekday
        # as the day you were born
        if d_day == new_d_day:

            # add to the list of true birthdate
            true_BD.append(new_birthday)
        else:
            pass
        j += 1

    return true_BD


def main():
    # Get the birth date
    birthdate = "1996-11-12"

    # year_limit = input("search limit from your birthday- ")
    dates = true_birthdays(birthdate)

    print(dates)


# Driver's code
main()
