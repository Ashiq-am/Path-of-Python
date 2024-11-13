import urllib.request
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'


file_Path = 'research_Paper_2.pdf'
urllib.request.urlretrieve(url, file_Path)
