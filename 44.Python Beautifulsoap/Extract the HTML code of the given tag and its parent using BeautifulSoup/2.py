# getting the h1 with id as firstHeading and printing it
title = soup.find("h1", attrs={"id": 'firstHeading'})
print(title)
