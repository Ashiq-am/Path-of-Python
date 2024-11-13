# link for extract html data
# Making a GET request

def getdata(url):
    r = requests.get(url)
    return r.text
