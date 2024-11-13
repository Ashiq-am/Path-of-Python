# since we need only first five coins
for x in range(1, 6):
    table = data.find_all('tr')[x]
    c = table.find_all('td')

    for x in c:
        print(x.text, end=' ')
    print('')
