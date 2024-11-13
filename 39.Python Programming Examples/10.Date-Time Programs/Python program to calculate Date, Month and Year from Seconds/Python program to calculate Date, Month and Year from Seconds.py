# function to get num of
# days in the year
# if leap year then 366
# else 365
def dayInYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 366
            else:
                return 365
        else:
            return 366
    else:
        return 365


# counting the years after 1947
def getYear(days):
    year = 1946
    while True:
        year += 1
        dcnt = dayInYear(year)
        if days >= dcnt:
            days -= dcnt
        else:
            break
    return year, days


# counting the number of months
def monthCnt(days, year):
    if days == 0:
        return 1, 0
    else:
        month_num = 1
        months = [31, 28, 31, 30, 31,
                  30, 31, 31, 30, 31,
                  30, 31]
        if dayInYear(year) == 366:
            months[1] = 29
        for day in months:
            if day < days:
                month_num += 1
                days -= day
            else:
                break
        return month_num, days


# getting date using number of seconds
def getDate(num_sec):
    # converting seconds into days
    days_sec = 24 * 60 * 60
    days = num_sec // days_sec
    day_started = False

    # if some seconds are more
    if days % days_sec != 0:
        day_started = True

    # getting year
    year, days = getYear(days)

    # getting month
    month, days = monthCnt(days, year)

    if day_started or num_sec == 0:
        days += 1

    # preparing date_format
    date = ""
    if month < 10:
        date = date + "0" + str(month)
    else:
        date = date + str(month)

    date = date + "-"

    if days < 10:
        date = date + "0" + str(days)
    else:
        date = date + str(days)

    date = date + "-"

    date = date + str(year)

    return date


# Driver Code

# returns 01-01-1970
date_format = getDate(0)
print(date_format)

# returns 11-29-1973
date_format = getDate(123456789)
print(date_format)

# returns 12-22-2282
date_format = getDate(9876543210)
print(date_format)
