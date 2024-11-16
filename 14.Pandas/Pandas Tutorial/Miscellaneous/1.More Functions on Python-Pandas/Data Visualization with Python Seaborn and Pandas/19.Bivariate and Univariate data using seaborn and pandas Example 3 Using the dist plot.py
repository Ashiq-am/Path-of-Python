# import module
import seaborn as sns
import pandas

# read top 5 column
data = pandas.read_csv("nba.csv").head()

sns.distplot( data['Age'])
