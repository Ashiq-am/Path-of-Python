import csv
import re


def tsv_to_csv(tsv_file, csv_file):
	with open(tsv_file, 'r', encoding='utf-8') as tsvfile:
		tsv_content = tsvfile.readlines()

	with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
		csvwriter = csv.writer(csvfile)
		for line in tsv_content:
			row = re.split(r'\t', line.strip())
			csvwriter.writerow(row)


# Example usage
tsv_to_csv('index.tsv', 'index.csv')
print('successfully converted')
