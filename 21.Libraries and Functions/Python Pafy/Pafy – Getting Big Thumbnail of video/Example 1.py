# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vG2PNdI8axo"

# getting video
video = pafy.new(url)

# getting big thumbnail of the video
value = video.bigthumb

# printing the value
print("Big Thumb : " + value)
