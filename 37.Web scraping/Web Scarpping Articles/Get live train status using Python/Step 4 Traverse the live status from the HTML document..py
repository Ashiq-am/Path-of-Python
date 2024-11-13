# traverse the live status from
# this Html code
data = []
for item in soup.find_all('script', type="application/ld+json"):
	data.append(item.get_text())

# convert into dataframe
df = pd.read_json (data[2])

# display this column of
# dataframe
print(df["mainEntity"][0])
