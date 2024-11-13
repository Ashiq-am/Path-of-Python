# create object
soup = BeautifuSoup(r.text, "html.parser")

# find title
title = soup.find("title")

# find heading
heading = soup.find("h1")

print(title)
