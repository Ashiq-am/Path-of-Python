import pandas as pds

# reading the XLSX file
file =('Acoustic_Extinguisher_Fire_Dataset/\
Acoustic_Extinguisher_Fire_Dataset.xlsx')
newData = pds.read_excel(file)

# displaying the contents of the XLSX file
newData.head()
