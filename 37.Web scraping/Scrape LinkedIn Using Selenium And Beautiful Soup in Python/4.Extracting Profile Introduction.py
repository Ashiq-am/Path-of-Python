# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

print(intro)
