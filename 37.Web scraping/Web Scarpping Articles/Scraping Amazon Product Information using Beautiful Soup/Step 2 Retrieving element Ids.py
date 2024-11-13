try:
    title = soup.find("span",
                      attrs={"id": 'productTitle'})
    title_value = title.string


    title_string = title_value.strip().replace(',', '')


except AttributeError:
    title_string = "NA"

print("product Title = ", title_string)
