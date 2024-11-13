import csv

def tsv_to_csv(tsv_file, csv_file):
	with open(tsv_file, 'r', newline='', encoding='utf-8') as tsvfile:
		tsvreader = csv.reader(tsvfile, delimiter='\t')

		with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
			csvwriter = csv.writer(csvfile)
			csvwriter.writerows(tsvreader)


# Example usage
tsv_to_csv('index.tsv', 'index.csv')
print('successfully converted')
