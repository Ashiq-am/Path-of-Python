# find the Html tag
# with find()
# and convert into string
data_str = ""
for item in soup.find_all("div", class_="NAURX0ARMmhJ5eqxQrlQW"):
    data_str = data_str + item.get_text()

print(data_str)
