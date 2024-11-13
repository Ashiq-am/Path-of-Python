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
