# importing pafy
import pafy

# url of video
url = "https://www.youtube.com / watch?v = mmjDZGSr7EA"

# instant created
video = pafy.new(url)

# getting number of likes
count = video.viewcount

# showing likes
print("View Count : " + str(count))
