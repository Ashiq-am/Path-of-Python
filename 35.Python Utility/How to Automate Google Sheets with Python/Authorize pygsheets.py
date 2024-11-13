# Importing required library
import pygsheets

# Create the Client
# Enter the name of the downloaded KEYS
# file in service_account_file
client = pygsheets.authorize(service_account_file="gfg-pygsheets-demo-e3d0c0e482af.json")

# Sample command to verify successful
# authorization of pygsheets
# Prints the names of the spreadsheet
# shared with or owned by the service
# account
print(client.spreadsheet_titles())
