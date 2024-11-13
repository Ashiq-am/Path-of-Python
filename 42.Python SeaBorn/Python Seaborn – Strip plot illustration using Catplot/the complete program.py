# importing modules
import pandas as pnd
import matplotlib.pyplot as plt
import seaborn as sbn



# fetching data from the url
url_data='http://bit.ly/2cLzoxH'

# using pandas for reading the data file
# storing the data in input_data variable
input_data=pnd.read_csv(url_data)



# using seaborn module to show the relation betwwen
# categorical variables and numerical variables
sbn.catplot(x='continent', y='lifeExp', data=input_data)
