# Import following modules
import urllib.request
import pandas as pd
from pushbullet import PushBullet

# Get Access Token from pushbullet.com
Access_token = "Your Access Token"

# Authentication
pb = PushBullet(Access_token)

# All pushes created by you
all_pushes = pb.get_pushes()

# Get the latest push
latest_one = all_pushes[0]

# Fetch the latest file URL link
url = latest_one['file_url']

# Create a new text file for storing
# all the chats
Text_file = "All_Chats.txt"

# Retrieve all the data store into
# Text file
urllib.request.urlretrieve(url, Text_file)

# Create an empty chat list
chat_list = []

# Open the Text file in read mode and
# read all the data
with open(Text_file, mode='r', encoding='utf8') as f:
    # Read all the data line-by-line
    data = f.readlines()

# Excluded the first item of the list
# first items contains some garbage
# data
final_data_set = data[1:]

# Run a loop and read all the data
# line-by-line
for line in final_data_set:
    # Extract the date, time, name,
    # message
    date = line.split(",")[0]
    tim = line.split("-")[0].split(",")[1]
    name = line.split(":")[1].split("-")[1]
    messag = line.split(":")[2][:-1]

    # Append all the data in a List
    chat_list.append([date, tim, name, messag])

# Create a dataframe, for storing
# all the data in a excel file
df = pd.DataFrame(chat_list,
                  columns=['Date', 'Time',
                           'Name', 'Message'])
df.to_excel("BackUp.xlsx", index=False)
