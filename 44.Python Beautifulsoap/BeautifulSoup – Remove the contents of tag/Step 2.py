# creating a soup
soup = BeautifulSoup(text,"html.parser")

# printing the content in h1 tag
print(f"Content of h1 tag is: {soup.h1}")
