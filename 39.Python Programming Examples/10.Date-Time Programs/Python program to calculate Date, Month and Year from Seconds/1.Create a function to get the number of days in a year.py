# function to get number of
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
