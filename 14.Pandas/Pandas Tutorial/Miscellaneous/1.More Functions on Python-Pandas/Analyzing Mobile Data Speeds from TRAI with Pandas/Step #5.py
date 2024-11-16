# filter out the operator and technology
# first as this will be common for all
filtered = df[(df['Service Provider'] == CONST_OPERATOR)
              & (df['Technology'] == CONST_TECHNOLOGY)]

# iterate through each of the states
for state in states:

    # create new dataframe which contains
    # only the data of the current state
    base = filtered[filtered['State'] == state]

    # filter only download speeds based on test type
    down = base[base['Test Type'] == 'download']

    # filter only upload speeds based on test type
    up = base[base['Test Type'] == 'upload']

    # calculate mean of speeds in Data Speed
    # column using the Pandas.mean() method
    avg_down = down['Data Speed'].mean()

    # calculate mean of speeds
    # in Data Speed column
    avg_up = up['Data Speed'].mean()

    # discard values if mean is not a number(nan)
    # and append only the valid ones
    if (pd.isnull(avg_down) or pd.isnull(avg_up)):
        down, up = 0, 0

    else:
        final_states.append(state)
        final_download_speeds.append(avg_down)
        final_upload_speeds.append(avg_up)

        # print output upto 2 decimal places
        print(str(state) + ' -- Avg. Download: ' +
              str('%.2f' % avg_down) +
              ' Avg. Upload: ' + str('%.2f' % avg_up))
