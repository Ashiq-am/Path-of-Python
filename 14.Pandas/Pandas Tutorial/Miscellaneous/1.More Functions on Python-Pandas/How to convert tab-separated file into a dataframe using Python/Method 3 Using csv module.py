import csv
file_path = "file.tsv"
with open(file_path, 'r') as file:
	reader = csv.reader(file, delimiter='\t')
	df = pd.DataFrame(reader)
df.head()
