# input the date and split it to day, month and year
day, month, year = map(int, input().split('/'))

if month == 2:

    # check for February
    if year % 4 != 0:
        d_max = 28
    else:
        d_max = 29

elif month in [4, 6, 9, 11]:

    # check the months with 30 days
    d_max = 30

else:
    d_max = 31

if 1 <= day <= d_max and 1 <= month <= 12:

    # increment the date since it is a
    # valid date
    if day == d_max:
        day = 1
        if month == 12:

            # If this block is enterred,
            # then it is the last day of
            # the year
            month = 1
            year += 1
        else:

            # If this block is enterred,
            # then it is the last day of
            # the month
            month += 1
    else:

        # If this block is enterred, then it
        # is NOT the last day of the month
        day += 1
    print(str(day) + "/" + str(month) + "/" + str(year))
else:
    print("Invalid date")
