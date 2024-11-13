# Replace "YEAR" by the year you
# want to get data from. Eg. "2018"
url = 'https://summerofcode.withgoogle.com/archive/YEAR/organizations/'

# Creating a response object
# from the given url
res = requests.get(url)

# We'll be using the Archive page
# of GSoC's website as our source.
# Checking the url's status
res.raise_for_status()
