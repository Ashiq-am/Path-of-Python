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
