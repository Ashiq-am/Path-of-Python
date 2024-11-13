# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vVSKoLJmn8w&t = 13s"

# getting video
video = pafy.new(url)

# getting extra large thumbnail of the video
value = video.bigthumbhd

# printing the value
print("Extra Large Thumbnail : " + value)
