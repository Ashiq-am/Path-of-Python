# importing required module
import pandas as pd
import re

# Creating df
# Reading data from Excel
data = pd.read_excel("Email_sample.xlsx")
print("Original DataFrame")
print(data)

# Create column for
# each type of Email
data['Google-mail'] = None
data['Yahoo-mail'] = None

# set index
index_set = data.columns.get_loc('E-mail')
index_gmail = data.columns.get_loc('Google-mail')
index_yahoo = data.columns.get_loc('Yahoo-mail')

# define Email pattern
google_pattern = r'gmail.com'
yahoo_pattern = r'yahoo.com'

# Searching the email
# Store into DataFrame
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
