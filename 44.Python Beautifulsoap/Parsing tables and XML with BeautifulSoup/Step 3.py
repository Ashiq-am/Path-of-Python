# find all tables
find_table = file.find('table', class_='numpy-table')
rows = find_table.find_all('tr')
