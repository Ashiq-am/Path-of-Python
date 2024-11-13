mydatastr = ''

# Filter converted data
for table in soup.find_all("div", class_="D(ib) Va(m) Maw(65%) Ov(h)"):
	mydatastr += table.get_text()

# Display output
print(mydatastr)
