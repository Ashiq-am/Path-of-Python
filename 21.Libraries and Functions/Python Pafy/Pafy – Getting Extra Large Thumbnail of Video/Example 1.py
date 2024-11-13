# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting extra large thumbnail of the video
value = video.bigthumbhd

# printing the value
print("Extra Large Thumbnail : " + value)
