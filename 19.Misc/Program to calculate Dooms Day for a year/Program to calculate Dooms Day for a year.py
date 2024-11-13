def dooms_day(year):
    # dictionary to store days
    # value of anchor day can be known
    dict_day = {0: "Sunday",
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday"}

    # gregorian calender repeats
    # every 400 years
    k = year % 400

    # decide the anchor day
    if (k >= 0 and k < 100):
        anchor = 2

    elif (k >= 100 and k < 200):
        anchor = 0

    elif (k >= 200 and k < 300):
        anchor = 5

    else:
        anchor = 3

    y = year % 100

    # dooms day formula by Conway
    doomsday = ((y // 12 + y % 12 + (y % 12) // 4) % 7 + anchor) % 7

    return dict_day[doomsday]


# Driver code
year = 1966
print("Doomsday in the year % s = % s" % (year,dooms_day(year)))
