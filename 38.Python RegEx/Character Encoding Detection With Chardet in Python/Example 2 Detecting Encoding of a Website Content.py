import requests
import chardet

# Fetch the web page content
response = requests.get('https://www.geeksforgeeks.org/')
html_content = response.content

# Detect the encoding
result = chardet.detect(html_content)
print(result['encoding'])
