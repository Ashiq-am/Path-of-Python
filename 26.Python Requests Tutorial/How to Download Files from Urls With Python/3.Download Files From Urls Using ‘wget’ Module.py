import wget
url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'


file_Path = 'research_Paper_3.pdf'
wget.download(url, file_Path)
print('downloaded')
