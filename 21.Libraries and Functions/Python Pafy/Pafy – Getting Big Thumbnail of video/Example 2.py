# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = vVSKoLJmn8w&t = 13s"

# getting video
video = pafy.new(url)

# getting big thumbnail of the video
value = video.bigthumb

# printing the value
print("Big Thumb : " + value)
