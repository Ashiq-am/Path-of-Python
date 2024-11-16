for row in range(0, len(data)):
    Date = re.search(date_pattern, data.iat[row, index_set]).group()
    data.iat[row, index_date] = Date

# show the Dataframe
data
