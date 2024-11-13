# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# instant created
video = pafy.new(url)

# getting title
value = video.title

# showing likes
print("Title : " + str(value))
