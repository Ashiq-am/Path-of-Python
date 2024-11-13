# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vVSKoLJmn8w&t = 13s"

# getting video
video = pafy.new(url)

# getting thumbnail of the video
value = video.thumb

# printing the value
print("Thumbnail : " + value)
