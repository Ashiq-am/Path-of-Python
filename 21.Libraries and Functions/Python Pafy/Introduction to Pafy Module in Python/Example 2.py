# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = mmjDZGSr7EA"

# instant created
video = pafy.new(url)

# getting thumb image
count = video.thumb

# showing likes
print("Thumb Image : " + str(count))
