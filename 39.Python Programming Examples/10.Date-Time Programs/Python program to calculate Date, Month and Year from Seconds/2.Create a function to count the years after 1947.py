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
