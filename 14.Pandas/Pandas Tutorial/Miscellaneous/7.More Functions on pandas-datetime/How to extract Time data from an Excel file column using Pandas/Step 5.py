# searching the entire DataFrame
# with Time pattern
for row in range(0, len(data)):
    time = re.search(time_pattern,
                     data.iat[row, index_set]).group()

    data.iat[row, index_time] = time

print("Final DataFrame")
data
