# to iterate excel file one by one
# inside the folder
for file in filenames:
    # combining multiple excel worksheets
    # into single data frames
    df = pd.concat(pd.read_excel(file, sheet_name=None),
                   ignore_index=True, sort=False)

    # Appending excel files one by one
    finalexcelsheet = finalexcelsheet.append(
        df, ignore_index=True)
