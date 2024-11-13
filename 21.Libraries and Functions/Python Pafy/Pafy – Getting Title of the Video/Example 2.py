# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vVSKoLJmn8w&t = 13s"

# getting video
video = pafy.new(url)

# getting title of the video
value = video.title

# printing the value
print("Title : " + value)
