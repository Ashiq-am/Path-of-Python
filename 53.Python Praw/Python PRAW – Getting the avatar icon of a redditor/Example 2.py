# importing the module
import praw
import PIL
import urllib

# initialize with appropriate values
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = ""

# creating an authorized reddit instance
reddit = praw.Reddit(client_id = client_id,
					client_secret = client_secret,
					username = username,
					password = password,
					user_agent = user_agent)

# the name of the redditor
redditor_name = "AutoModerator"

# instantiating the Redditor class
redditor = reddit.redditor(redditor_name)

# fetching the URL of the image
url = redditor.icon_img

print("The URL of the icon image of " + redditor_name +
	" is : \n" + url)

# displaying the image
urllib.request.urlretrieve(url, "reddit.png")
img = PIL.Image.open("reddit.png")
img.show()
