from bs4 import BeautifulSoup
with open('file1.xml', 'r') as file1, open('file2.xml', 'r') as file2:
	soup1 = BeautifulSoup(file1, 'xml')
	soup2 = BeautifulSoup(file2, 'xml')
	if soup1.prettify() == soup2.prettify():
		print("XML files are same.")
	else:
		print("XML files are different.")
