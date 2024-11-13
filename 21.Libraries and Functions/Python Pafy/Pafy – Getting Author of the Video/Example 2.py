# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vVSKoLJmn8w&t = 13s"

# getting video
video = pafy.new(url)

# getting author of the video
value = video.author

# printing the value
print("Author : " + value)
