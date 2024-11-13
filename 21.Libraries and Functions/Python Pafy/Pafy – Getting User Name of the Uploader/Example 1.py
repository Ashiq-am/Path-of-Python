# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting username of the video's uploader
value = video.username

# printing the value
print("Username : " + value)
