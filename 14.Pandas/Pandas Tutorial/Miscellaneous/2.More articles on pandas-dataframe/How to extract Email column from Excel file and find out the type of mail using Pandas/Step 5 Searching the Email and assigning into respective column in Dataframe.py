# Search the Email in DataFrame and store
for row in range(0, len(data)):

    if re.search(google_pattern,
                 data.iat[row, index_set]) == None:
        data.iat[row, index_gmail] = 'Account not belongs to Google'

    else:
        gmail = re.search(google_pattern,
                          data.iat[row, index_set]).group()
        data.iat[row, index_gmail] = "Google-Mail"

    if re.search(yahoo_pattern,
                 data.iat[row, index_set]) == None:
        data.iat[row, index_yahoo] = 'Account not belongs to Yahoo'

    else:
        yahoo = re.search(yahoo_pattern,
                          data.iat[row, index_set]).group()
        data.iat[row, index_yahoo] = "Yahoo-Mail"

data
