# Load the Monthly Sunspots dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/monthly-sunspots.csv"
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')
print(data)
