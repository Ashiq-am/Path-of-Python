from bs4 import BeautifulSoup

soup=BeautifulSoup(page.content,"html.parser")

# fetching the <meta> tag's
# charset attribute
# of the content above
tag=soup.meta['charset']

print("Encoding method :",tag)
