# Create a list of User-Agents
import requests


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 \
Safari/537.2'}
response = requests.get(url, headers=header)


# Use UserAgent from fake_useragent module
import requests
from fake_useragent import UserAgent


ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
response = requests.get(url, headers=header)
