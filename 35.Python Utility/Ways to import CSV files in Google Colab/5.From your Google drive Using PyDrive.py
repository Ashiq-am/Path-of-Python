link = 'https://drive.google.com/file/d/1KiYk09VqGI6tjNpalom5wI90GrC2p-lz/view'

import pandas as pd

# to get the id part of the file
id = link.split("/")[-2]

downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('xclara.csv')

df = pd.read_csv('xclara.csv')
print(df)
